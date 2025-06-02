import streamlit as st
import pandas as pd
import plotly.express as px
from code import (
    n,
    calcular_media,
    calcular_mediana,
    calcular_variancia,
    calcular_desvio,
    calcular_coef_variacao,
    calcular_moda,
)

st.set_page_config(page_title="Agrupamento Discreto", layout="centered")
st.title("Agrupamento Discreto")
st.markdown(
    """
    Insira os valores de Xi e suas frequências (Fi) para calcular:
    - Média
    - Mediana
    - Moda
    - Variância
    - Desvio Padrão
    - Coeficiente de Variação
    """
)

unidade = st.text_input("Unidade de medida (ex.: kg, m, cm, °C) — deixe em branco se não houver", value="").strip()

linhas = st.number_input(
    "Quantos elementos (Xi) farão parte da sua tabela de amostras?",
    min_value=1,
    step=1,
    format="%d"
)

st.markdown("---")

st.subheader("Insira os valores de Xi e Fi")
Xi_inputs = []
Fi_inputs = []

for i in range(int(linhas)):
    cols = st.columns(2)
    xi_val = cols[0].number_input(
        label=f"Xi do elemento #{i+1} ({unidade})" if unidade else f"Xi do elemento #{i+1}",
        key=f"xi_{i}",
        min_value=0,
        step=1,
        format="%d"
    )
    fi_val = cols[1].number_input(
        label=f"Fi do elemento #{i+1}",
        key=f"fi_{i}",
        min_value=0,
        step=1,
        format="%d"
    )
    Xi_inputs.append(xi_val)
    Fi_inputs.append(int(fi_val))

st.markdown("---")

if st.button("Calcular Estatísticas"):
    dados = {
        'Xi': [],
        'Fi': [],
        'Xi X Fi': [],
        'Fac': [],
        '(Xi - x̄)^2 Fi': []
    }

    fac_acumulada = 0
    for xi, fi in zip(Xi_inputs, Fi_inputs):
        dados['Xi'].append(xi)
        dados['Fi'].append(fi)
        dados['Xi X Fi'].append(round(xi * fi, 2))
        fac_acumulada += fi
        dados['Fac'].append(fac_acumulada)

    total_n = n(dados)
    media_valor = calcular_media(dados)
    calcular_variancia(dados, media_valor)
    variancia_total = round(sum(dados['(Xi - x̄)^2 Fi']) / (total_n - 1), 2) if total_n > 1 else 0.0
    desvio = calcular_desvio(variancia_total)
    coef_var = calcular_coef_variacao(desvio, media_valor)
    mediana_valor = calcular_mediana(dados)
    tipo_moda, lista_moda, fi_moda = calcular_moda(dados)

    df = pd.DataFrame(dados)

    resumo = {
        'N': [total_n],
        f'Média ({unidade})': [f"{media_valor}{unidade}" if unidade else f"{media_valor}"],
        f'Mediana ({unidade})': [f"{mediana_valor}{unidade}" if unidade else f"{mediana_valor}"],
        f'Moda ({unidade})': [f"{", ".join(str(x) for x in lista_moda)} (Fi={fi_moda})" if lista_moda else "Amodal"],
        f'Variância ({unidade}²)': [f"{variancia_total}{unidade}²" if unidade else f"{variancia_total}"],
        f'Desvio Padrão ({unidade})': [f"{desvio}{unidade}" if unidade else f"{desvio}"],
        'Coef. Variação (%)': [f"{coef_var}%"]
    }
    df_resumo = pd.DataFrame(resumo)

    st.subheader("Tabela de Dados Detalhada")
    st.dataframe(df, use_container_width=True)

    st.subheader("Resumo Estatístico")
    st.dataframe(df_resumo, use_container_width=True)

    st.markdown("---")
    st.write(f"**Total de Observações (N):** {total_n}")
    st.write(f"**Tipo de Moda:** {tipo_moda}")
    if tipo_moda != 'Amodal':
        st.write(f"**Valores Modal (Xi):** {', '.join(str(x) for x in lista_moda)} (Fi = {fi_moda})")
    else:
        st.write("**Amostra Amodal (sem moda definida)**")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Distribuição das Frequências Individuais")
        freq_df = pd.DataFrame({'Xi': dados['Xi'], 'Fi': dados['Fi']})
        st.dataframe(freq_df, use_container_width=True)

    with col2:
        fig = px.pie(freq_df, names='Xi', values='Fi')
        st.plotly_chart(fig, use_container_width=True)