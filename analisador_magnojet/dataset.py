from pathlib import Path

from analisador_magnojet import RAIZ
from analisador_magnojet.arquivos import ler_dados

DATASET = RAIZ / "dataset"
CLASSES = ler_dados(DATASET / "classes.json")
EXTENSOES = ("jpg", "jpeg", "png", "webp", "bmp", "tiff", "tif")


def listar_imagens(pasta):
    return sorted(
        caminho for caminho in Path(pasta).rglob("*")
        if caminho.is_file() and caminho.suffix.lower()[1:] in EXTENSOES
    )


def caminho_rotulo(imagem):
    imagem = Path(imagem)
    return imagem.parent.parent / "labels" / imagem.with_suffix(".txt").name


def ler_rotulo(imagem):
    linhas = caminho_rotulo(imagem).read_text(encoding="ascii").splitlines()
    return [
        (int(indice), *(float(valor) for valor in valores))
        for indice, *valores in (linha.split() for linha in linhas if linha.strip())
    ]


def selecionar(grupo, classe=None):
    manifesto = ler_dados(DATASET / "manifesto.json")
    if grupo == "online":
        return listar_imagens(DATASET / "online/images")
    if grupo == "ampliado":
        return [DATASET / item["imagem"] for item in manifesto["variacoes"]]
    imagens = [DATASET / item["imagem"] for item in manifesto["base"]]
    if grupo == "classe":
        indice = CLASSES.index(classe)
        return [
            imagem for imagem in imagens
            if (rotulos := ler_rotulo(imagem)) and all(rotulo[0] == indice for rotulo in rotulos)
        ]
    if grupo == "rapido":
        return imagens[:3]
    return imagens
