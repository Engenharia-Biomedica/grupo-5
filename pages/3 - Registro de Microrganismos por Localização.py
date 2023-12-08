import pandas as pd
import streamlit as st

# Configuração da página Streamlit
st.set_page_config(page_title = 'Registro de Microrganismos por Localização', page_icon = '🦠', initial_sidebar_state = 'collapsed')

# Cabeçalho da aplicação
st.header('Painel de Monitoramento Microbiológico')

# Carregamento dos dados e coordenadas das unidades de atendimento a partir de arquivos CSV
dados = pd.read_csv("sample_data_clean.csv", sep = ",")
coordenadas = pd.read_csv("coordenadas_Einstein.csv", sep = ",")

# Subcabeçalho
st.header('Registro de Microrganismos por Localização', divider = 'rainbow')

# Verifica se os DataFrames estão vazios
if dados.empty or coordenadas.empty:

    st.error('Erro ao carregar dados. Certifique-se de que os arquivos estão corretos e contêm dados válidos.')

else:

    # Filtro para o microrganismo
    ds_micro_organismo = st.selectbox('Selecione um microrganismo:', list(dados['ds_micro_organismo'].unique()))

    # Filtragem dos dados com base no microrganismo selecionado
    dados_filt = dados.query(f"ds_micro_organismo == '{ds_micro_organismo}'")
    coordenadas_filt = coordenadas.merge(dados_filt, left_on = 'nome_unidade', right_on = 'ds_unidade_coleta')

    # Verifica se o DataFrame filtrado está vazio
    if coordenadas_filt.empty:

        st.warning(f'Não há unidades com registro para o microrganismo {ds_micro_organismo}.')

    else:

        # Agrupamento por unidade de coleta e contagem de registros
        contagem_registro = coordenadas_filt['ds_unidade_coleta'].value_counts().reset_index()
        contagem_registro.columns = ['Local', 'Registros']

        # Exibição dos dados em uma tabela
        st.subheader('Registros por Local:')
        st.dataframe(contagem_registro)

        # Conversão dos valores para garantir que as coordenadas sejam interpretadas corretamente
        coordenadas_filt = coordenadas_filt.astype({'latitude': float, 'longitude': float})

        st.subheader('Mapa:')
        # Exibição do mapa com as coordenadas das unidades de coleta
        st.map(data = coordenadas_filt, latitude = 'latitude', longitude = 'longitude')