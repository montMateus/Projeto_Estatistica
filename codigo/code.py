from math import sqrt

def n(dados: dict) -> int:
    return sum(dados['Fi'])

def calcular_media(dados: dict) -> float:
    total = n(dados)
    return round(sum(dados['Xi X Fi']) / total, 2) if total > 0 else 0.0

def calcular_mediana(dados: dict) -> float:
    total = n(dados)
    if total == 0:
        return 0.0

    em1 = total // 2
    em2 = em1 + 1 if total % 2 == 0 else em1

    x_em1 = None
    x_em2 = None

    for i in range(len(dados['Fac'])):
        if dados['Fac'][i] >= em1 and x_em1 is None:
            x_em1 = dados['Xi'][i]
        if dados['Fac'][i] >= em2:
            x_em2 = dados['Xi'][i]
            break

    if x_em1 is None or x_em2 is None:
        return 0.0

    return round((x_em1 + x_em2) / 2, 2)

def calcular_variancia(dados: dict, media_valor: float) -> None:
    dados['(Xi - x̄)^2 Fi'] = []
    for i in range(len(dados['Xi'])):
        xi = dados['Xi'][i]
        fi = dados['Fi'][i]
        var = round(((xi - media_valor) ** 2) * fi, 2)
        dados['(Xi - x̄)^2 Fi'].append(var)

def calcular_desvio(variancia_valor: float) -> float:
    return round(sqrt(variancia_valor), 2)

def calcular_coef_variacao(desvio: float, media_valor: float) -> float:
    return round((desvio / media_valor) * 100, 2) if media_valor != 0 else 0.0

def calcular_moda(dados: dict) -> (str, list, int):
    if not dados['Fi']:
        return ("Amodal", [], 0)

    fi_max = max(dados['Fi'])
    count_fi_max = dados['Fi'].count(fi_max)
    xi_moda = []

    if count_fi_max == len(dados['Xi']):
        tipo = 'Amodal'
    elif count_fi_max == 1:
        tipo = 'Unimodal'
    elif count_fi_max == 2:
        tipo = 'Bimodal'
    elif count_fi_max == 3:
        tipo = 'Trimodal'
    else:
        tipo = 'Multimodal'

    if tipo != 'Amodal':
        for i, fi in enumerate(dados['Fi']):
            if fi == fi_max:
                xi_moda.append(dados['Xi'][i])

    return (tipo, xi_moda, fi_max)