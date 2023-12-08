import pandas as pd
import streamlit as st

# Configuração da página Streamlit
st.set_page_config(page_title = 'Antibióticos e Resistência Bacteriana', page_icon = '🦠', initial_sidebar_state = 'collapsed')

# Cabeçalho da aplicação
st.header('Painel de Monitoramento Microbiológico')

# Carregamento dos dados a partir de um arquivo CSV
dados = pd.read_csv("sample_data_clean.csv", sep = ",")

# Subcabeçalho
st.subheader('Antibióticos e Resistência Bacteriana', divider = 'rainbow')

# Verifica se o DataFrame está vazio
if dados.empty:

    st.error('Erro ao carregar dados. Certifique-se de que o banco de dados está correto e contém dados válidos.')

else:

    # Filtro para o tipo de bactéria
    ds_micro_organismo = st.selectbox('Selecione o tipo de bactéria:', ['Todos'] + list(dados['ds_micro_organismo'].unique()))

    # Filtro para o tipo de antibiótico associado ao microorganismo
    ds_antibiotico_microorganismo = st.selectbox('Selecione o tipo de antibiótico:', ['Todos'] + list(dados['ds_antibiotico_microorganismo'].unique()))

    # Lógica de filtro de dados
    dados_filt = dados[((ds_micro_organismo == 'Todos') | (dados['ds_micro_organismo'] == ds_micro_organismo)) &
                       ((ds_antibiotico_microorganismo == 'Todos') | (dados['ds_antibiotico_microorganismo'] == ds_antibiotico_microorganismo))]

    # Verifica se o DataFrame filtrado está vazio
    if dados_filt.empty:

        st.warning('Nenhum dado correspondente aos filtros selecionados.')

    else:

        # Cálculo da frequência para fármacos utilizados
        contagem_frequencia = dados_filt['ds_antibiotico_microorganismo'].value_counts().reset_index()
        contagem_frequencia.columns = ['Fármacos Utilizados', 'Frequência de uso']

        # Exibição dos dados em uma tabela
        st.subheader('Frequência dos Fármacos Utilizados:')
        st.dataframe(contagem_frequencia)

        # Exibição dos dados em um gráfico de barras
        st.subheader('Gráfico de Barras para os Fármacos Utilizados:')
        st.bar_chart(contagem_frequencia.set_index('Fármacos Utilizados'))

        # Cálculo da frequência para tipo de resistência
        contagem_frequencia_resistencia = dados_filt['cd_interpretacao_antibiograma'].value_counts().reset_index()
        contagem_frequencia_resistencia.columns = ['Tipo de Resistência', 'Frequência']

        # Exibição dos dados em uma tabela
        st.subheader('Frequência dos Tipos de Resistência:')
        st.dataframe(contagem_frequencia_resistencia)

        # Exibição dos dados em um gráfico de barras
        st.subheader('Gráfico de Barras para os Tipos de Resistência:')
        st.bar_chart(contagem_frequencia_resistencia.set_index('Tipo de Resistência'))