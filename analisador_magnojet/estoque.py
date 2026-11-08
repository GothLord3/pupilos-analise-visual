from decimal import Decimal

from filelock import FileLock

from analisador_magnojet import RAIZ
from analisador_magnojet.arquivos import ler_dados, salvar_json
from analisador_magnojet.dataset import CLASSES

ESTOQUE = RAIZ / "estoque.json"


def consultar():
    if ESTOQUE.exists():
        return ler_dados(ESTOQUE)
    return {}


def salvar(classe, quantidade, valor):
    centavos = int(Decimal(str(valor)).quantize(Decimal("0.01")) * 100)
    if classe not in CLASSES or quantidade < 0 or centavos < 0:
        raise ValueError("Informe uma classe válida, quantidade e valor positivos ou zero.")
    with FileLock(str(ESTOQUE) + ".lock"):
        estoque = consultar()
        estoque[classe] = dict(componente="Bico de pulverização", modelo="PBIA",
                             classe=classe, estoque=quantidade, valor_unitario_centavos=centavos)
        salvar_json(ESTOQUE, estoque)
