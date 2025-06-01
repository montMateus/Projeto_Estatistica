import pandas as pd
from math import sqrt
from collections import Counter

def gerar_dados():

    dados = {
        'Xi': [],
        'Fi': [],
        'Fac': [],
        'Xi X Fi': [],
        '(Xi - x̄)^2 Fi': [],
        #'N': [],
    }
    
    return dados

def n(dados: dict):
    return sum(dados['Fi'])

def media(dados: dict):
    valor_n = n(dados)
    media = round(sum(dados['Xi X Fi']) / valor_n, 2)
    print(media)
    return media

def mediana(dados: dict):
    valor_n = n(dados)
    n2 = valor_n / 2
    
    for idx, fac in enumerate(dados['Fac']):
        if fac >= n2:
            mediana_x = dados['Xi'][idx]
            print(f'Mediana encontrada: {mediana_x}')
            return mediana_x

    print('Mediana não encontrada.')
    return None


def varianca(media: float, dados: dict):  
    for i in range(len(dados['Xi'])):
        xi = dados['Xi'][i]
        fi = dados['Fi'][i]
        var = round(((xi - media) ** 2 * fi), 2)
        dados['(Xi - x̄)^2 Fi'].append(var)

def desvio_padrao(varianca: float):
    return round(sqrt(varianca), 2)

def coef_variacao(desvio_padrao: float, media: float):
    coef = round((desvio_padrao / media), 2) * 100
    return  coef

def moda(dados:dict):
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
    elif count_fi_max > 3:
        tipo_moda = 'Multimodal'

    if tipo_moda == 'Amodal':
        print(f'Amostra {tipo_moda}')
    else:
        for i in range(len(dados['Fi'])):
            if dados['Fi'][i] == fi_max:
                xi_moda.append(dados['Xi'][i])
        print(f'Amostra {tipo_moda} | Elemento(s) Xi: {xi_moda} | Fi da moda: {fi_max}')
        
while True:

    dados = gerar_dados()

    try:
        opcao = int(input(
            'Digite o número da opção escolhida: \n'
            '[1] - Criar tabela de amostras \n'
            '[2] - Finalizar programa \n'
        ))
    except ValueError:
        print('Por favor, insira um número válido.')
        continue

    if opcao == 1:
        while True:
            try:
                linhas = int(input('Quantos elementos farão parte da sua tabela de amostras? \n'))
                break
            except ValueError:
                print('Por favor, insira um número válido.')

        for i in range(linhas):
            while True:
                try:
                    xi = int(input(f'Digite o valor para o {i + 1}º elemento Xi: '))
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
            xi_x_fi = round((xi * fi), 2)
            dados['Xi X Fi'].append(xi_x_fi)

            if len(dados['Fac']) == 0:
                fac = fi
            else:
                fac = dados['Fac'][-1] + fi
            dados['Fac'].append(fac)

        media = media(dados)
        variancia = varianca(media, dados=dados)
        moda(dados)

        df = pd.DataFrame(dados)
        print(mediana(dados))
        print(f'mediana: {df.median()}')
        print(df)

    elif opcao == 2:
        print('Programa finalizado.')
        break
    else:
        print('Por favor, insira uma opção válida (1 ou 2).')