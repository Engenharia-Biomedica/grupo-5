import pandas as pd
import streamlit as st

# Header
st.header('Resistência das Bactérias')

# Upload do arquivo CSV
upload_arquivo = st.file_uploader('Escolha um arquivo (.csv):', type='csv')

# Subheader
st.header('Série Quantitativa', divider='rainbow')

if upload_arquivo is not None:

    # Leitura do arquivo CSV
    arquivo = pd.read_csv(upload_arquivo)

    # Criando um filtro de dados para o tipo de bactéria
    ds_micro_organismo = st.selectbox('Selecione o tipo de bactéria:', ['Todos'] + list(arquivo['ds_micro_organismo'].unique()))
    
    if ds_micro_organismo == 'Todos':

        arquivo_filt = arquivo

    else:

        arquivo_filt = arquivo[arquivo['ds_micro_organismo'] == ds_micro_organismo]

    # Cálculo da frequência
    contagem_frequencia = arquivo_filt['cd_interpretacao_antibiograma'].value_counts().reset_index()

 # Renomeando as colunas para a exibição no Streamlit
    contagem_frequencia.columns = ['Resistência', 'Frequência']

# Exibição dos dados
    st.subheader('Contagem de Frequência:')
    st.dataframe(contagem_frequencia)

 # Exibição visual dos dados (gráfico de barras)
    st.subheader('Gráfico de Barras:')
    st.bar_chart(contagem_frequencia.set_index('Resistência'))