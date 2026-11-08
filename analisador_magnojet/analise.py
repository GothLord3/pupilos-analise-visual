import os
from collections import Counter
from datetime import datetime
from pathlib import Path
from time import perf_counter
from uuid import uuid4

from PIL import Image, ImageDraw, ImageFont, ImageOps

from analisador_magnojet import RAIZ
from analisador_magnojet.arquivos import calcular_hash, ler_dados, salvar_json
from analisador_magnojet.dataset import CLASSES

ANALISES = RAIZ / "runs/analises"
MODELOS = RAIZ / "modelos"
CORES = ("#14699e", "#8b288f", "#076b52", "#ab421c", "#265cb9", "#805b00", "#995076", "#424e60")


def catalogo_modelos():
    return ler_dados(MODELOS / "catalogo.json")


def carregar_modelo(pesos):
    cache = RAIZ / "runs/cache-yolo"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("YOLO_CONFIG_DIR", str(cache))
    os.environ.setdefault("YOLO_OFFLINE", "true")
    import torch
    from ultralytics import YOLO

    torch.set_num_threads(min(4, os.cpu_count() or 1))
    modelo = YOLO(str(pesos))
    if modelo.task != "detect":
        raise ValueError("Os pesos precisam pertencer a um detector YOLO.")
    return modelo


def detectar(modelo, imagem, confianca, tamanho):
    resultado = modelo.predict(
        imagem, conf=confianca, imgsz=tamanho, iou=0.50, agnostic_nms=True,
        device="cpu", verbose=False,
    )[0]
    deteccoes = []
    for caixa in resultado.boxes:
        classe = resultado.names[int(caixa.cls.item())].replace("PBIA-25", "PBIA-025")
        if classe in CLASSES:
            deteccoes.append(dict(classe=classe, confianca=float(caixa.conf.item()),
                                  caixa=caixa.xyxy[0].tolist()))
    deteccoes.sort(key=lambda objeto: (objeto["caixa"][1], objeto["caixa"][0]))
    return [dict(id=numero, **objeto) for numero, objeto in enumerate(deteccoes, 1)]


def desenhar(imagem, deteccoes):
    desenho = ImageDraw.Draw(imagem)
    fonte = ImageFont.load_default(size=max(14, min(40, imagem.width // 45)))
    traco = max(2, imagem.width // 280)
    for objeto in deteccoes:
        cor = CORES[CLASSES.index(objeto["classe"])]
        x1, y1, x2, y2 = objeto["caixa"]
        texto = f'{objeto["id"]} {objeto["classe"]} {objeto["confianca"]:.0%}'
        desenho.rectangle((x1, y1, x2, y2), outline=cor, width=traco)
        largura = desenho.textlength(texto, font=fonte) + 8
        _, topo, _, base = desenho.textbbox((0, 0), texto, font=fonte, anchor="lt")
        altura = base - topo + 8
        x = max(0, min(x1, imagem.width - largura))
        y = max(0, y1 - altura)
        desenho.rectangle((x, y, x + largura, y + altura), fill=cor)
        desenho.text((x + 4, y + 4), texto, fill="white", font=fonte, anchor="lt")


def analisar(entradas, modelo_id=None, confianca=None, tamanho=None, destino=ANALISES):
    catalogo = catalogo_modelos()
    modelo_id = modelo_id or catalogo["oficial"]
    config = catalogo["modelos"][modelo_id]
    pesos = MODELOS / config["pesos"]
    confianca = config["confianca"] if confianca is None else confianca
    tamanho = config["tamanho"] if tamanho is None else tamanho
    if not 0 < confianca <= 1 or tamanho < 32 or tamanho % 32:
        raise ValueError("Use confiança entre 0 e 1 e tamanho múltiplo de 32.")
    if not entradas:
        raise ValueError("Selecione pelo menos uma imagem.")

    modelo = carregar_modelo(pesos)
    nomes = {nome.replace("PBIA-25", "PBIA-025") for nome in modelo.names.values()}
    if nomes != set(CLASSES):
        raise ValueError("O detector precisa usar as oito classes PB-IA do dataset.")
    data = datetime.now().astimezone()
    pasta = Path(destino) / f'{data:%Y%m%d-%H%M%S}-{uuid4().hex[:8]}'
    pasta.mkdir(parents=True)
    imagens, erros = [], []
    totais = Counter()
    for numero, (nome, entrada) in enumerate(entradas, 1):
        try:
            with Image.open(entrada) as origem:
                imagem = ImageOps.exif_transpose(origem).convert("RGB")
        except (OSError, ValueError, Image.DecompressionBombError) as erro:
            erros.append(dict(imagem=nome, erro=str(erro)))
            continue
        inicio = perf_counter()
        caixas = detectar(modelo, imagem, confianca, tamanho)
        segundos = perf_counter() - inicio
        contagem = Counter(objeto["classe"] for objeto in caixas)
        totais.update(contagem)
        marcado = f"imagem-{numero:03d}.jpg"
        desenhar(imagem, caixas)
        imagem.save(pasta / marcado, quality=93)
        imagens.append(dict(origem=nome, imagem=marcado, largura=imagem.width,
                            altura=imagem.height, segundos=segundos, total=len(caixas),
                            por_classe=dict(contagem), deteccoes=caixas))

    resumo = dict(imagens=len(imagens), total=sum(totais.values()), por_classe=dict(totais),
                  imagens_sem_deteccao=sum(item["total"] == 0 for item in imagens),
                  imagens_com_erro=len(erros))
    salvar_json(pasta / "resultados.json", dict(
        data=data.isoformat(timespec="seconds"), modelo=modelo_id, pesos=pesos.name,
        pesos_sha256=calcular_hash(pesos), confianca=confianca, tamanho=tamanho,
        iou_nms=0.50, dispositivo="cpu", resumo=resumo, imagens=imagens, erros=erros,
    ))
    return pasta
