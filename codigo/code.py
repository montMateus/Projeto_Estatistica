import pandas as pd
from math import sqrt

def gerar_dados():
    return {
        'Xi': [],
        'Fi': [],
        'Fac': [],
        'Xi X Fi': [],
        '(Xi - x̄)^2 Fi': []
    }

def n(dados: dict):
    return sum(dados['Fi'])

def media(dados: dict):
    valor_n = n(dados)
    media_calc = round(sum(dados['Xi X Fi']) / valor_n, 2)
    print(f'Média: {media_calc}')
    return media_calc

def mediana(dados: dict):
    valor_n = n(dados)
    print(f'n: {valor_n}')

    em1 = valor_n // 2
    em2 = em1 + 1 if valor_n % 2 == 0 else em1  

    x_em1 = None
    x_em2 = None

    for i in range(len(dados['Fac'])):
        if dados['Fac'][i] >= em1 and x_em1 is None:
            x_em1 = dados['Xi'][i]
        if dados['Fac'][i] >= em2:
            x_em2 = dados['Xi'][i]
            break

    me = (x_em1 + x_em2) / 2
    print(f'Mediana: {me}')
    return me

def calcular_varianca(media_valor: float, dados: dict):
    for i in range(len(dados['Xi'])):
        xi = dados['Xi'][i]
        fi = dados['Fi'][i]
        var = round(((xi - media_valor) ** 2) * fi, 2)
        dados['(Xi - x̄)^2 Fi'].append(var)

def desvio_padrao(variancia_valor: float):
    return round(sqrt(variancia_valor), 2)

def coef_variacao(desvio: float, media_valor: float):
    coef = round((desvio / media_valor) * 100, 2)
    return coef

def moda(dados: dict):
    xi_moda = []
    tipo_moda = ''

    fi_max = max(dados['Fi'])
    count_fi_max = dados['Fi'].count(fi_max)

    if count_fi_max == len(dados['Xi']):
        tipo_moda = 'Amodal'
    elif count_fi_max == 1:
        tipo_moda = 'Unimodal'
    elif count_fi_max == 2:
        tipo_moda = 'Bimodal'
    elif count_fi_max == 3:
        tipo_moda = 'Trimodal'
    else:
        tipo_moda = 'Multimodal'

    if tipo_moda == 'Amodal':
        print(f'Amostra {tipo_moda}')
    else:
        for i in range(len(dados['Fi'])):
            if dados['Fi'][i] == fi_max:
                xi_moda.append(dados['Xi'][i])
        print(f'Amostra {tipo_moda} | Elemento(s) Xi: {xi_moda} | Fi da moda: {fi_max}')

def exibir_tamanhos(dados: dict):
    for k, v in dados.items():
        print(f'{k}: {len(v)} elementos')

while True:
    dados = gerar_dados()

    try:
        opcao = int(input(
            '\nDigite o número da opção escolhida: \n'
            '[1] - Criar tabela de amostras \n'
            '[2] - Finalizar programa \n'
        ))
    except ValueError:
        print('Por favor, insira um número válido.')
        continue

    if opcao == 1:
        unidade = ''
        usar_unidade = input('Deseja adicionar uma unidade de medida aos elementos Xi? (s/n): ').strip().lower()
        if usar_unidade == 's':
            unidade = input('Digite a unidade de medida (ex.: kg, m, cm, ºC): ').strip()
        else:
            print('Nenhuma unidade foi escolhida')

        while True:
            try:
                linhas = int(input('Quantos elementos farão parte da sua tabela de amostras? \n'))
                break
            except ValueError:
                print('Por favor, insira um número válido.')

        for i in range(linhas):
            while True:
                try:
                    xi = float(input(f'Digite o valor para o {i + 1}º elemento Xi ({unidade}): ' if unidade else f'Digite o valor para o {i + 1}º elemento Xi: '))
                    break
                except ValueError:
                    print('Por favor, insira um número válido.')

            while True:
                try:
                    fi = int(input(f'Digite a frequência individual do {i + 1}º elemento Xi: '))
                    break
                except ValueError:
                    print('Por favor, insira um número válido.')

            dados['Xi'].append(xi)
            dados['Fi'].append(fi)
            dados['Xi X Fi'].append(round(xi * fi, 2))

            fac = fi if len(dados['Fac']) == 0 else dados['Fac'][-1] + fi
            dados['Fac'].append(fac)

        # Cálculos
        media_valor = media(dados)
        calcular_varianca(media_valor, dados)
        moda(dados)
        mediana_valor = mediana(dados)
        variancia_total = round(sum(dados['(Xi - x̄)^2 Fi']) / (n(dados) - 1), 2)
        desvio = desvio_padrao(variancia_total)
        coef = coef_variacao(desvio, media_valor)

        # Criar DataFrame
        df = pd.DataFrame(dados)

        # Adicionar estatísticas ao DataFrame
        resumo = {
            'N': n(dados),
            f'Média ({unidade})': str(media_valor) + unidade,
            f'Mediana ({unidade})': str(mediana_valor) + unidade,
            f'Moda ({unidade})': [max(dados["Fi"])],
            f'Variância ({unidade}²)': str(variancia_total) + unidade + '²',
            f'Desvio Padrão ({unidade})': str(desvio) + unidade,
            'Coef. Variação (%)': coef
        }
        df_resumo = pd.DataFrame(resumo)

        print("\nTabela de Dados:")
        print(df)
        print("\nResumo Estatístico:")
        print(df_resumo)

    elif opcao == 2:
        print('Programa finalizado.')
        break
    else:
        print('Por favor, insira uma opção válida (1 ou 2).')
