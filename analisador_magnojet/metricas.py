"""Critérios de correspondência e medidas de detecção e contagem."""

from collections import Counter


def intersecao_uniao(caixa_a, caixa_b):
    intersecao = max(
        0, min(caixa_a[2], caixa_b[2]) - max(caixa_a[0], caixa_b[0])
    ) * max(0, min(caixa_a[3], caixa_b[3]) - max(caixa_a[1], caixa_b[1]))
    uniao = (
        (caixa_a[2] - caixa_a[0]) * (caixa_a[3] - caixa_a[1])
        + (caixa_b[2] - caixa_b[0]) * (caixa_b[3] - caixa_b[1])
        - intersecao
    )
    return intersecao / uniao if uniao > 0 else 0


def comparar(reais, previsoes, limiar, iou_minimo=0.5):
    if not 0 < iou_minimo <= 1:
        raise ValueError("A IoU mínima deve estar entre zero exclusivo e um.")
    previsoes = [previsao for previsao in previsoes if previsao["confianca"] >= limiar]
    candidatos = sorted(
        [
            (
                intersecao_uniao(real["caixa"], previsao["caixa"]),
                indice_real,
                indice_previsto,
            )
            for indice_real, real in enumerate(reais)
            for indice_previsto, previsao in enumerate(previsoes)
            if real["classe"] == previsao["classe"]
        ],
        reverse=True,
    )
    usados_reais, usados_previstos = set(), set()
    for sobreposicao, indice_real, indice_previsto in candidatos:
        if (
            sobreposicao >= iou_minimo
            and indice_real not in usados_reais
            and indice_previsto not in usados_previstos
        ):
            usados_reais.add(indice_real)
            usados_previstos.add(indice_previsto)
    acertos = len(usados_reais)
    return dict(
        reais=len(reais),
        previstos=len(previsoes),
        verdadeiros_positivos=acertos,
        falsos_positivos=len(previsoes) - acertos,
        falsos_negativos=len(reais) - acertos,
        erro_absoluto_contagem=abs(len(reais) - len(previsoes)),
        contagem_exata=len(reais) == len(previsoes),
        identificacao_completa=acertos == len(reais) == len(previsoes),
        contagem_por_classe_exata=Counter(real["classe"] for real in reais)
        == Counter(previsao["classe"] for previsao in previsoes),
    )


def resumir(linhas):
    acertos = sum(linha["verdadeiros_positivos"] for linha in linhas)
    extras = sum(linha["falsos_positivos"] for linha in linhas)
    omissoes = sum(linha["falsos_negativos"] for linha in linhas)
    return dict(
        imagens=len(linhas),
        objetos_reais=acertos + omissoes,
        objetos_previstos=acertos + extras,
        verdadeiros_positivos=acertos,
        falsos_positivos=extras,
        falsos_negativos=omissoes,
        precisao=acertos / (acertos + extras) if acertos + extras else 0,
        revocacao=acertos / (acertos + omissoes) if acertos + omissoes else 0,
        f1=(
            2 * acertos / (2 * acertos + extras + omissoes)
            if 2 * acertos + extras + omissoes
            else 0
        ),
        mae_contagem=(
            sum(linha["erro_absoluto_contagem"] for linha in linhas) / len(linhas)
            if linhas
            else 0
        ),
        imagens_contagem_exata=sum(linha["contagem_exata"] for linha in linhas),
        imagens_identificacao_completa=sum(
            linha["identificacao_completa"] for linha in linhas
        ),
        imagens_contagem_por_classe_exata=sum(
            linha["contagem_por_classe_exata"] for linha in linhas
        ),
    )
