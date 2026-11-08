import argparse
from pathlib import Path

from analisador_magnojet.analise import analisar
from analisador_magnojet.arquivos import ler_dados
from analisador_magnojet.dataset import EXTENSOES, listar_imagens


def principal():
    parser = argparse.ArgumentParser(prog="Analisador Magnojet")
    parser.add_argument("origem", type=Path, help="Imagem ou pasta de imagens.")
    parser.add_argument("--modelo", help="Identificador listado por scripts.modelos.")
    parser.add_argument("--confianca", type=float)
    parser.add_argument("--tamanho", type=int, choices=(320, 480, 640, 800, 960))
    args = parser.parse_args()
    if args.origem.is_dir():
        imagens = listar_imagens(args.origem)
    elif args.origem.is_file() and args.origem.suffix.lower()[1:] in EXTENSOES:
        imagens = [args.origem]
    else:
        parser.error("Escolha uma imagem compatível ou uma pasta existente.")
    try:
        pasta = analisar([(str(foto), foto) for foto in imagens], args.modelo,
                         args.confianca, args.tamanho)
    except (KeyError, ValueError, OSError) as erro:
        parser.error(str(erro))
    resumo = ler_dados(pasta / "resultados.json")["resumo"]
    print(pasta)
    print(f'{resumo["imagens"]} imagem(ns), {resumo["total"]} detecção(ões), '
          f'{resumo["imagens_com_erro"]} erro(s).')
    return int(resumo["imagens"] == 0)


if __name__ == "__main__":
    raise SystemExit(principal())
