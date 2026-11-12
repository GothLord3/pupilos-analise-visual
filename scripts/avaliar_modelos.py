import argparse
import json

from PIL import Image

from analisador_magnojet.analise import MODELOS, carregar_modelo, catalogo_modelos, detectar
from analisador_magnojet.arquivos import ler_dados
from analisador_magnojet.dataset import CLASSES, DATASET, ler_rotulo, selecionar
from analisador_magnojet.metricas import comparar, resumir

LIMIARES = (0.01, 0.025, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)


def prever(modelo, imagens, tamanho, confianca):
    casos = []
    for imagem in imagens:
        with Image.open(imagem) as fonte:
            foto = fonte.convert("RGB")
        reais = [
            dict(classe=CLASSES[indice], caixa=[
                (x - w / 2) * foto.width, (y - h / 2) * foto.height,
                (x + w / 2) * foto.width, (y + h / 2) * foto.height,
            ])
            for indice, x, y, w, h in ler_rotulo(imagem)
        ]
        previstos = detectar(modelo, foto, confianca, tamanho)
        casos.append((reais, previstos))
    return casos


def medir(casos, limiar):
    return resumir([comparar(reais, previstos, limiar) for reais, previstos in casos])


def avaliar(pesos, tamanho, limiar=None):
    manifesto = ler_dados(DATASET / "manifesto.json")
    modelo = carregar_modelo(pesos)
    validacao = [DATASET / item["imagem"] for item in manifesto["base"] if item["divisao"] == "val"]
    minimo = min(LIMIARES) if limiar is None else limiar
    casos_val = prever(modelo, validacao, tamanho, minimo)
    if limiar is None:
        medidas = {candidato: medir(casos_val, candidato) for candidato in LIMIARES}
        limiar = max(medidas, key=lambda valor: (medidas[valor]["imagens_identificacao_completa"],
                                                medidas[valor]["f1"], valor))
    teste = [DATASET / item["imagem"] for item in manifesto["base"] if item["divisao"] == "test"]
    alteradas = [DATASET / item["imagem"] for item in manifesto["variacoes"] if item.get("teste")]
    metricas = {"validacao_base": medir(casos_val, limiar)}
    for nome, imagens in (("teste_base", teste), ("teste_ampliado", alteradas),
                         ("teste_online", selecionar("online"))):
        metricas[nome] = medir(prever(modelo, imagens, tamanho, limiar), limiar)
    return limiar, metricas


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reavalia os pesos nos conjuntos fixos da entrega.")
    catalogo = catalogo_modelos()
    parser.add_argument("--modelo", choices=catalogo["modelos"])
    parser.add_argument("--pesos", type=str)
    parser.add_argument("--tamanho", type=int)
    parser.add_argument("--confianca", type=float)
    args = parser.parse_args()
    if args.pesos:
        if args.modelo or args.tamanho is None or args.confianca is None:
            parser.error("Use --pesos com --tamanho e --confianca, sem --modelo.")
        pesos, tamanho, confianca = args.pesos, args.tamanho, args.confianca
    else:
        modelo = args.modelo or catalogo["oficial"]
        config = catalogo["modelos"][modelo]
        pesos = MODELOS / config["pesos"]
        tamanho, confianca = config["tamanho"], config["confianca"]
    _, metricas = avaliar(pesos, tamanho, confianca)
    print(json.dumps(metricas, ensure_ascii=False, indent=2))
