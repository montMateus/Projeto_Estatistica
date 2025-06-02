# Agrupamento Discreto

Este projeto utiliza Streamlit para criar uma aplicação web interativa. Siga os passos abaixo para configurar e executar o código.

## Pré-requisitos

Antes de começar, você precisará ter o Python e o `venv` instalados em sua máquina.

**Instalar o Python**: Certifique-se de que o Python está instalado. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).

## Passo a Passo

### Criar um Ambiente Virtual

Abra o terminal (ou prompt de comando) e navegue até o diretório do seu projeto. Em seguida, crie um ambiente virtual com o seguinte comando:

``` python -m venv venv ```

### Ative o ambiente virtual

#### Windows
``` venv\Scripts\activate ```

#### macOS e Linux
``` source venv/bin/activate ```

### Instalar os Pacotes Necessários e Executar

``` pip install streamlit plotly.express pandas ```

```` python -m streamlit run ./codigo/page.py ````

ou

``` streamlit run ./codigo/page.py ``` 