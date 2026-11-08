from io import BytesIO

import streamlit as st

from analisador_magnojet.analise import ANALISES, analisar, catalogo_modelos
from analisador_magnojet.arquivos import ler_dados
from analisador_magnojet.dataset import CLASSES, EXTENSOES
from analisador_magnojet.estoque import consultar, salvar


def exibir_resultado(pasta, chave):
    arquivo = pasta / "resultados.json"
    resultado = ler_dados(arquivo)
    resumo = resultado["resumo"]
    st.caption(f'{resultado["data"]} | {resultado["modelo"]} | {pasta}')
    colunas = st.columns(3)
    colunas[0].metric("Fotos analisadas", resumo["imagens"])
    colunas[1].metric("Detecções PB-IA", resumo["total"])
    colunas[2].metric("Fotos sem detecção", resumo["imagens_sem_deteccao"])
    if resumo["por_classe"]:
        st.table([{"Classe": classe, "Quantidade": total}
                  for classe, total in sorted(resumo["por_classe"].items())])
    if resultado["imagens"]:
        imagens = resultado["imagens"]
        indice = st.selectbox("Foto do lote", range(len(imagens)),
                             format_func=lambda i: imagens[i]["origem"], key=chave)
        item = imagens[indice]
        st.image(str(pasta / item["imagem"]), caption=item["origem"], width="stretch")
        st.caption(f'{item["largura"]} × {item["altura"]} px | {item["segundos"]:.3f} s')
        if item["deteccoes"]:
            st.table([{"Nº": objeto["id"], "Classe": objeto["classe"],
                       "Confiança": f'{objeto["confianca"]:.1%}',
                       "Caixa em pixels (x1, y1, x2, y2)": ", ".join(
                           str(round(v)) for v in objeto["caixa"])}
                      for objeto in item["deteccoes"]])
    if resultado["erros"]:
        st.warning("Fotos que não puderam ser lidas.")
        st.table(resultado["erros"])
    with st.expander("Configuração da análise"):
        st.json({chave: resultado[chave] for chave in (
            "pesos", "pesos_sha256", "confianca", "tamanho", "iou_nms", "dispositivo"
        )})
    st.download_button("Baixar JSON de resultados", arquivo.read_bytes(),
                       file_name="resultados.json", mime="application/json", key=f"json-{chave}")


def tela_analise():
    catalogo = catalogo_modelos()
    oficial = catalogo["oficial"]
    modelo_id = st.selectbox("Modelo", [oficial] + sorted(set(catalogo["modelos"]) - {oficial}),
                            format_func=lambda nome: f"{nome} (oficial)" if nome == oficial else nome)
    modelo = catalogo["modelos"][modelo_id]
    certeza = st.slider("Confiança mínima (%)", 1.0, 100.0, modelo["confianca"] * 100, step=0.5,
                       key=f"certeza-{modelo_id}", help="Aumente para exigir mais confiança em cada detecção.")
    tamanhos = (320, 480, 640, 800, 960)
    tamanho = st.selectbox("Resolução de análise", tamanhos, index=tamanhos.index(modelo["tamanho"]),
                           key=f"resolucao-{modelo_id}", help="Uma resolução maior pode levar mais tempo.")
    modo = st.radio("Origem das fotos", ["Enviar fotos", "Câmera"], horizontal=True)
    if modo == "Enviar fotos":
        arquivos = st.file_uploader("Escolha uma ou mais fotos", type=EXTENSOES, accept_multiple_files=True)
        entradas = [(arquivo.name, arquivo) for arquivo in arquivos]
    else:
        if "fotos" not in st.session_state:
            st.session_state.fotos = []
            st.session_state.camera_id = 0
        captura = st.camera_input("Fotografar", key=f"camera-{st.session_state.camera_id}")
        if st.button("Adicionar foto ao lote", disabled=captura is None):
            st.session_state.fotos.append(captura.getvalue())
            st.session_state.camera_id += 1
            st.rerun()
        st.caption(f"{len(st.session_state.fotos)} foto(s) no lote.")
        if st.button("Limpar lote", disabled=not st.session_state.fotos):
            st.session_state.fotos.clear()
            st.session_state.camera_id += 1
            st.rerun()
        entradas = [(f"camera-{n:03d}.jpg", BytesIO(foto))
                    for n, foto in enumerate(st.session_state.fotos, 1)]
        if captura is not None:
            entradas.append((f"camera-{len(entradas) + 1:03d}.jpg", captura))
    if st.button("Analisar", type="primary", disabled=not entradas):
        try:
            with st.spinner("Analisando fotos..."):
                st.session_state.resultado = analisar(entradas, modelo_id, certeza / 100, tamanho)
        except (OSError, ValueError, RuntimeError) as erro:
            st.error(str(erro))
    if "resultado" in st.session_state:
        pasta = st.session_state.resultado
        if (pasta / "resultados.json").is_file():
            exibir_resultado(pasta, f"analise-{pasta.name}")


def tela_historico():
    pastas = sorted((arquivo.parent for arquivo in ANALISES.glob("*/resultados.json")), reverse=True)
    if pastas:
        pasta = st.selectbox("Registro", pastas, format_func=lambda p: p.name)
        exibir_resultado(pasta, f"historico-{pasta.name}")
    else:
        st.info("Ainda não há análises salvas.")


def moeda(centavos):
    return "R$ " + f"{centavos / 100:,.2f}".translate(str.maketrans(",.", ".,"))


def tela_estoque():
    itens = consultar()
    if itens:
        st.table([{"Componente": item["componente"], "Modelo": item["modelo"],
                   "Classe": item["classe"], "Estoque": item["estoque"],
                   "Valor unitário": moeda(item["valor_unitario_centavos"]),
                   "Subtotal": moeda(item["estoque"] * item["valor_unitario_centavos"])}
                  for item in sorted(itens.values(), key=lambda item: item["classe"])])
    st.metric("Valor do estoque", moeda(sum(
        item["estoque"] * item["valor_unitario_centavos"] for item in itens.values()
    )))
    st.caption("Componente: bico de pulverização | Modelo: PBIA")
    classe = st.selectbox("Classe", CLASSES)
    item = itens.get(classe, {"estoque": 0, "valor_unitario_centavos": 0})
    with st.form(f"estoque-{classe}"):
        quantidade = st.number_input("Quantidade", min_value=0, value=item["estoque"], step=1)
        valor = st.number_input("Valor unitário (R$)", min_value=0.0, step=0.01, format="%.2f",
                                value=item["valor_unitario_centavos"] / 100)
        if st.form_submit_button("Salvar estoque"):
            salvar(classe, quantidade, valor)
            st.rerun()


st.set_page_config(page_title="Analisador Magnojet")
st.title("Analisador Magnojet")
pagina = st.sidebar.radio("Seção", ["Análise", "Histórico", "Estoque e financeiro"])
if pagina == "Análise":
    tela_analise()
elif pagina == "Histórico":
    tela_historico()
else:
    tela_estoque()
