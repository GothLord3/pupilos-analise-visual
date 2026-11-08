import argparse
import csv
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DATASET = RAIZ / "dataset"
PERFIS = {
    "base": {"imgsz": 320, "optimizer": "AdamW", "lr0": 0.002, "freeze": 0},
    "ampliado": {"imgsz": 320, "optimizer": "AdamW", "lr0": 0.001, "freeze": 5},
    "ajuste": {"imgsz": 480, "optimizer": "SGD", "lr0": 0.004, "freeze": 5},
}


def treinar(perfil, inicial, epocas, dispositivo):
    pasta = RAIZ / "runs/treinos"
    pasta.mkdir(parents=True, exist_ok=True)
    cache = RAIZ / "runs/cache-yolo"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("YOLO_CONFIG_DIR", str(cache))
    os.environ.setdefault("YOLO_OFFLINE", "true")
    import torch
    from ultralytics import YOLO

    torch.set_num_threads(min(4, os.cpu_count() or 1))
    manifesto = json.loads((DATASET / "manifesto.json").read_text(encoding="utf8"))
    classes = json.loads((DATASET / "classes.json").read_text(encoding="utf8"))
    nome = perfil + "-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    rodada = pasta / nome
    rodada.mkdir()
    for divisao in ("train", "val", "test"):
        imagens = [item["imagem"] for item in manifesto["base"] if item["divisao"] == divisao]
        if perfil != "base" and divisao == "train":
            imagens.extend(item["imagem"] for item in manifesto["variacoes"] if item["treino"])
        (rodada / f"{divisao}.txt").write_text(
            "".join(f"{(DATASET / imagem).as_posix()}\n" for imagem in imagens), encoding="utf8"
        )
    yaml = rodada / "dataset.yaml"
    yaml.write_text(
        json.dumps(dict(path=rodada.as_posix(), train="train.txt", val="val.txt",
                        test="test.txt", names=classes), indent=2), encoding="utf8"
    )
    modelo = YOLO(str(inicial))
    args = dict(batch=12, seed=42, workers=0, mosaic=0.0, hsv_h=0.0, hsv_s=0.0, hsv_v=0.0,
                degrees=0.0, translate=0.0, scale=0.0, fliplr=0.0, warmup_epochs=1.0,
                plots=False, amp=False, **PERFIS[perfil])
    modelo.train(data=str(yaml), project=str(pasta), name=nome, exist_ok=True,
                 epochs=epocas, device=dispositivo, **args)
    with (rodada / "results.csv").open(encoding="utf8") as csv_file:
        historico = list(csv.DictReader(csv_file))
    resumo = dict(perfil=perfil, inicial=inicial.name,
                  inicial_sha256=hashlib.sha256(inicial.read_bytes()).hexdigest(),
                  dados_sha256=hashlib.sha256((DATASET / "manifesto.json").read_bytes()).hexdigest(),
                  versao_torch=torch.__version__,
                  epocas=len(historico), dispositivo=dispositivo, configuracao=args,
                  metricas_validacao_por_epoca=historico)
    (rodada / "treino.json").write_text(json.dumps(resumo, indent=2) + "\n", encoding="utf8")
    print(rodada / "weights/best.pt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Treina um detector de bicos PB-IA.")
    parser.add_argument("perfil", choices=PERFIS)
    parser.add_argument("--inicial", type=Path, default=RAIZ / "modelos/yolo11n-coco.pt")
    parser.add_argument("--epocas", type=int, default=12)
    parser.add_argument("--dispositivo", default="cpu")
    args = parser.parse_args()
    treinar(args.perfil, args.inicial.resolve(), args.epocas, args.dispositivo)
