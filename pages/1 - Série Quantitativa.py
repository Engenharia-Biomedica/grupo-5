import pandas as pd
import streamlit as st

# Header
st.header('Painel de Monitoramento Microbiológico')

# Upload do arquivo CSV
dados = pd.read_csv("sample_data_clean.csv", sep=",")

if not dados.empty:
    # Subheader
    st.subheader('Antibióticos e Resistência Bacteriana')

    # Criando um filtro de dados para o tipo de bactéria
    ds_micro_organismo = st.selectbox('Selecione o tipo de bactéria:', ['Todos'] + list(dados['ds_micro_organismo'].unique()))

    # Criando um filtro de dados para o tipo de antibiótico
    ds_antibiotico_microorganismo = st.selectbox('Selecione o tipo de antibiótico:', ['Todos'] + list(dados['ds_antibiotico_microorganismo'].unique()))

    # Lógica de filtro de dados
    dados_filt = dados[((ds_micro_organismo == 'Todos') | (dados['ds_micro_organismo'] == ds_micro_organismo)) &
                       ((ds_antibiotico_microorganismo == 'Todos') | (dados['ds_antibiotico_microorganismo'] == ds_antibiotico_microorganismo))]

    if not dados_filt.empty:
        # Cálculo da frequência para fármacos utilizados
        contagem_frequencia = dados_filt['ds_antibiotico_microorganismo'].value_counts().reset_index()
        contagem_frequencia.columns = ['Fármacos Utilizados', 'Frequência de uso']

        # Exibição dos dados e gráfico de barras
        st.subheader('Frequência de Fármacos Utilizados:')
        st.dataframe(contagem_frequencia)
        st.subheader('Gráfico de Barras para Fármacos Utilizados:')
        st.bar_chart(contagem_frequencia.set_index('Fármacos Utilizados'))

        # Cálculo da frequência para tipo de resistência
        contagem_frequencia_resistencia = dados_filt['cd_interpretacao_antibiograma'].value_counts().reset_index()
        contagem_frequencia_resistencia.columns = ['Tipo de Resistência', 'Frequência']

        # Exibição dos dados e gráfico de barras
        st.subheader('Frequência do Tipo de Resistência:')
        st.dataframe(contagem_frequencia_resistencia)
        st.subheader('Gráfico de Barras para Tipo de Resistência:')
        st.bar_chart(contagem_frequencia_resistencia.set_index('Tipo de Resistência'))

    else:

        st.warning('Nenhum dado correspondente aos filtros selecionados.')

else:

    st.error('Erro ao carregar dados. Certifique-se de que o arquivo (.csv) está correto e contém dados válidos.')