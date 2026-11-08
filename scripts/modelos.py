import argparse
import json

from analisador_magnojet import RAIZ
from analisador_magnojet.analise import MODELOS, catalogo_modelos
from analisador_magnojet.arquivos import calcular_hash, ler_dados


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mostra pesos, configuração e avaliação dos modelos.")
    parser.add_argument("--modelo", help="Identificador de um modelo.")
    args = parser.parse_args()
    catalogo = catalogo_modelos()
    treinos = ler_dados(RAIZ / "docs/treinos.json")["modelos"]
    nomes = [args.modelo] if args.modelo else catalogo["modelos"]
    for nome in nomes:
        if nome not in catalogo["modelos"]:
            parser.error(f"Modelo desconhecido: {nome}")
        config = catalogo["modelos"][nome]
        caminho = MODELOS / config["pesos"]
        if calcular_hash(caminho) != config["sha256"]:
            raise SystemExit(f"Peso alterado: {caminho}")
        registro = {"modelo": nome, "oficial": nome == catalogo["oficial"], **config, **treinos[nome]}
        print(json.dumps(registro, ensure_ascii=False, indent=2))
