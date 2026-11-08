import json
import sys
from collections import Counter

from PIL import Image

from analisador_magnojet import RAIZ
from analisador_magnojet.arquivos import calcular_hash, ler_dados
from analisador_magnojet.dataset import CLASSES, DATASET, caminho_rotulo, ler_rotulo, listar_imagens


def conferir():
    manifesto = ler_dados(DATASET / "manifesto.json")
    base = manifesto["base"]
    variacoes = manifesto["variacoes"]
    online = ler_dados(DATASET / "online/fontes.json")
    assert len(base) == 84 and sum(item["tipo"] == "mista" for item in base) == 20
    assert len(CLASSES) == len(set(CLASSES)) == 8
    assert all(classe.startswith("PBIA-") for classe in CLASSES)
    divisao = {item["imagem"]: item["divisao"] for item in base}
    assert Counter(divisao.values()) == {"train": 59, "val": 19, "test": 6}
    originais = {RAIZ / item["original"] for item in base}
    assert len(originais) == 84 and originais == set(listar_imagens(RAIZ / "Bicos de Pulverização"))
    assert len({item["original_sha256"] for item in base}) == 84
    for item in base:
        assert calcular_hash(RAIZ / item["original"]) == item["original_sha256"], item["original"]
        assert len(ler_rotulo(DATASET / item["imagem"])) == item["caixas"], item["imagem"]
    grupos = {nome: {item["grupo"] for item in base if item["divisao"] == nome}
              for nome in ("train", "val", "test")}
    assert not (grupos["train"] & grupos["val"] or grupos["train"] & grupos["test"]
                or grupos["val"] & grupos["test"])
    for item in variacoes:
        origem, fundo = divisao[item["origem"]], divisao[item["fundo"]]
        assert item["treino"] == (origem == fundo == "train"), item["imagem"]
        if item.get("teste"):
            assert origem == fundo == "test", item["imagem"]
    nomes = [item["imagem"] for item in base + variacoes]
    nomes.extend(f'online/images/{item["arquivo"]}' for item in online)
    imagens = {DATASET / nome for nome in nomes}
    assert len(nomes) == len(imagens) and imagens == set(listar_imagens(DATASET))
    assert {caminho_rotulo(imagem) for imagem in imagens} == set(DATASET.rglob("*.txt"))
    contagem = Counter({classe: 0 for classe in CLASSES})
    negativos = 0
    for imagem in sorted(imagens):
        with Image.open(imagem) as foto:
            foto.load()
        rotulos = ler_rotulo(imagem)
        negativos += not rotulos
        for indice, x, y, w, h in rotulos:
            assert 0 <= indice < len(CLASSES) and 0 < w <= 1 and 0 < h <= 1, imagem
            assert 0 <= x <= 1 and 0 <= y <= 1, imagem
            assert x-w/2 >= -0.002 and y-h/2 >= -0.002, imagem
            assert x+w/2 <= 1.002 and y+h/2 <= 1.002, imagem
            if imagem.relative_to(DATASET).as_posix() in divisao:
                contagem[CLASSES[indice]] += 1
    return dict(
        originais=len(base), mistas=20, por_divisao=Counter(divisao.values()),
        fontes_de_rotulo=Counter(item["anotacao"] for item in base),
        caixas_base_por_classe=contagem,
        variacoes=Counter(item["transformacao"] for item in variacoes),
        variacoes_de_treino=sum(item["treino"] for item in variacoes),
        variacoes_de_teste=sum(item.get("teste", False) for item in variacoes),
        online=len(online), imagens_sem_caixas=negativos,
    )


if __name__ == "__main__":
    if sys.flags.optimize:
        raise SystemExit("Execute a conferência sem a opção -O.")
    print(json.dumps(conferir(), indent=2, ensure_ascii=False))
