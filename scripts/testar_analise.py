import argparse
import json

from analisador_magnojet import RAIZ
from analisador_magnojet.analise import analisar
from analisador_magnojet.arquivos import ler_dados
from analisador_magnojet.dataset import CLASSES, selecionar


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roda a análise em subconjuntos do dataset.")
    parser.add_argument("grupo", choices=("rapido", "base", "ampliado", "classe", "online"))
    parser.add_argument("--classe", choices=[*CLASSES, "todas"], default="todas")
    parser.add_argument("--modelo")
    args = parser.parse_args()
    if args.grupo != "classe" and args.classe != "todas":
        parser.error("Use --classe com o grupo classe.")
    classes = [None]
    if args.grupo == "classe":
        classes = CLASSES if args.classe == "todas" else [args.classe]
    for classe in classes:
        imagens = selecionar(args.grupo, classe)
        caminho = analisar([(foto.name, foto) for foto in imagens], args.modelo,
                           destino=RAIZ / "runs/testes")
        resumo = ler_dados(caminho / "resultados.json")["resumo"]
        print(f"{classe or args.grupo} | {caminho}")
        print(json.dumps(resumo, ensure_ascii=False))
        if resumo["imagens"] != len(imagens):
            raise SystemExit(1)
