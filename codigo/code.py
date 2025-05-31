import pandas as pd
from math import sqrt
from collections import Counter

def gerar_dados():

    dados = {
        'Xi': [],
        'Fi': [],
        'Fac': [],
        '(Xi - Media)^2 Fi': [],
        'N': [],
    }
    
    return dados

def varianca(media: float, dados: dict):  
    for i in range(len(dados['Xi'])):
        xi = dados['Xi'][i]
        fi = dados['Fi'][i]
        var = ((xi - media) ** 2) * fi
        dados['(Xi - Media)^2 Fi'].append(var)

def desvio_padrao(varianca: float):
    return sqrt(varianca)

def coef_variacao(desvio_padrao: float, media: float):
    coef = (desvio_padrao / media) * 100
    return coef

while True:

    dados = gerar_dados()

    try:
        opc = int(input(
            'Digite o número da opção escolhida: \n'
            '[1] - Criar tabela de amostras \n'
            '[2] - Finalizar programa \n'
        ))
    except ValueError:
        print('Por favor, insira um número válido.')
        continue

    if opc == 1:
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

            if len(dados['Fac']) == 0:
                fac = fi
            else:
                fac = dados['Fac'][-1] + fi
            dados['Fac'].append(fac)

        media = media(dados)
        variancia = varianca(media=10, dados=dados)

        df = pd.DataFrame(dados)
        print(df)

    elif opc == 2:
        print('Programa finalizado.')
        break
    else:
        print('Por favor, insira uma opção válida (1 ou 2).')