import hashlib
import json
from pathlib import Path
from uuid import uuid4


def ler_dados(caminho):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))


def salvar_json(caminho, dados):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_name(f".{caminho.name}.{uuid4().hex}.tmp")
    try:
        temporario.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf8",
        )
        temporario.replace(caminho)
    finally:
        temporario.unlink(missing_ok=True)


def calcular_hash(caminho):
    with Path(caminho).open("rb") as arquivo:
        return hashlib.file_digest(arquivo, "sha256").hexdigest()
