import argparse
import csv
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DATASET = RAIZ / "dataset"
CONFIGURACAO = {
    "imgsz": 800,
    "batch": 8,
    "optimizer": "SGD",
    "lr0": 0.002,
    "freeze": 0,
    "seed": 42,
    "workers": 0,
    "patience": 50,
    "mosaic": 0.0,
    "hsv_h": 0.0,
    "hsv_s": 0.0,
    "hsv_v": 0.3,
    "degrees": 8.0,
    "translate": 0.12,
    "scale": 0.3,
    "fliplr": 0.5,
    "warmup_epochs": 1.0,
    "plots": False,
    "amp": True,
    "deterministic": True,
}


def preparar_dataset(rodada):
    manifesto = json.loads((DATASET / "manifesto.json").read_text(encoding="utf8"))
    classes = json.loads((DATASET / "classes.json").read_text(encoding="utf8"))
    for divisao in ("train", "val", "test"):
        imagens = [item["imagem"] for item in manifesto["base"] if item["divisao"] == divisao]
        if divisao == "train":
            imagens.extend(item["imagem"] for item in manifesto["variacoes"] if item["treino"])
        (rodada / f"{divisao}.txt").write_text(
            "".join(f"{(DATASET / imagem).as_posix()}\n" for imagem in imagens),
            encoding="utf8",
        )
    yaml = rodada / "dataset.yaml"
    yaml.write_text(
        json.dumps({"path": rodada.as_posix(), "train": "train.txt", "val": "val.txt",
                    "test": "test.txt", "names": classes}, indent=2),
        encoding="utf8",
    )
    return yaml


def resultado_igual_ou_melhor(candidata, referencia):
    grupos = ("validacao_base", "teste_base", "teste_ampliado")
    return all(candidata[grupo]["f1"] >= referencia[grupo]["f1"] for grupo in grupos)


def treinar(inicial, epocas, dispositivo, configuracao=None):
    pasta = RAIZ / "runs/treinos"
    pasta.mkdir(parents=True, exist_ok=True)
    cache = RAIZ / "runs/cache-yolo"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("YOLO_CONFIG_DIR", str(cache))
    os.environ.setdefault("YOLO_OFFLINE", "true")

    import torch
    from ultralytics import YOLO
    from scripts.avaliar_modelos import avaliar

    torch.set_num_threads(min(4, os.cpu_count() or 1))
    nome = "ajuste-oficial-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    rodada = pasta / nome
    rodada.mkdir()
    yaml = preparar_dataset(rodada)

    parametros = dict(CONFIGURACAO)
    if configuracao:
        parametros.update({chave: valor for chave, valor in configuracao.items() if valor is not None})
    if str(dispositivo).lower() == "cpu":
        parametros["amp"] = False

    modelo = YOLO(str(inicial))
    modelo.train(
        data=str(yaml), project=str(pasta), name=nome, exist_ok=True,
        epochs=epocas, device=dispositivo, **parametros,
    )

    with (rodada / "results.csv").open(encoding="utf8") as csv_file:
        historico = list(csv.DictReader(csv_file))
    melhor_epoca = max(
        historico,
        key=lambda linha: float(linha.get("metrics/mAP50-95(B)") or 0),
        default={},
    )

    pesos_ajustados = rodada / "weights/best.pt"
    _, metricas_referencia = avaliar(inicial, 960, 0.50)
    _, metricas_ajustadas = avaliar(pesos_ajustados, 960, 0.50)
    aprovado = resultado_igual_ou_melhor(metricas_ajustadas, metricas_referencia)
    origem_final = pesos_ajustados if aprovado else inicial
    pesos_finais = rodada / "weights/modelo-final.pt"
    shutil.copy2(origem_final, pesos_finais)

    resumo = {
        "modelo_inicial": inicial.name,
        "epocas": len(historico),
        "dispositivo": dispositivo,
        "configuracao": parametros,
        "melhor_epoca": melhor_epoca,
        "metricas_referencia": metricas_referencia,
        "metricas_ajustadas": metricas_ajustadas,
        "ajuste_aprovado": aprovado,
        "pesos_finais": str(pesos_finais),
    }
    (rodada / "treino.json").write_text(
        json.dumps(resumo, ensure_ascii=False, indent=2) + "\n",
        encoding="utf8",
    )
    print(json.dumps(resumo, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ajusta e avalia o modelo oficial.")
    parser.add_argument("--inicial", type=Path, default=RAIZ / "modelos/Oficial-v1.pt")
    parser.add_argument("--epocas", type=int, default=14)
    parser.add_argument("--dispositivo", default="cpu")
    parser.add_argument("--imgsz", type=int)
    parser.add_argument("--batch", type=int)
    parser.add_argument("--optimizer", choices=("SGD", "Adam", "AdamW", "RMSProp"))
    parser.add_argument("--lr0", type=float)
    parser.add_argument("--freeze", type=int)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--patience", type=int)
    argumentos = parser.parse_args()
    configuracao = {
        nome: getattr(argumentos, nome)
        for nome in ("imgsz", "batch", "optimizer", "lr0", "freeze", "workers", "seed", "patience")
    }
    treinar(
        argumentos.inicial.resolve(), argumentos.epocas,
        argumentos.dispositivo, configuracao,
    )
