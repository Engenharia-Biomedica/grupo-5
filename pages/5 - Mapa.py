import pandas as pd
import streamlit as st

# Header
st.header('Painel de Monitoramento Microbiológico')

# Upload do arquivo CSV
upload_arquivo = st.file_uploader('Escolha um arquivo contendo os dados para serem analisados (.csv):', type='csv')
upload_coordenadas = st.file_uploader('Escolha um arquivo com as coordenadas das unidades de atendimento (.csv):', type='csv')

# Subheader
st.header('Mapa', divider='rainbow')

if upload_arquivo and upload_coordenadas is not None:

    # Leitura dos arquivos CSV
    arquivo = pd.read_csv(upload_arquivo)
    coordenadas = pd.read_csv(upload_coordenadas)

    # Criando um filtro de dados para o local de coleta
    ds_unidade_coleta = st.selectbox('Selecione o local de coleta: ', ['Todos'] + list(arquivo['ds_unidade_coleta'].unique()))

    if ds_unidade_coleta == 'Todos':

        arquivo_filt = arquivo
        coordenadas_filt = coordenadas  # Use todas as coordenadas

    else:

        arquivo_filt = arquivo[arquivo['ds_unidade_coleta'] == ds_unidade_coleta]
        coordenadas_filt = coordenadas[coordenadas['nome_unidade'] == ds_unidade_coleta]

    # Cálculo da frequência de bactérias
    contagem_frequencia_bacteria = arquivo_filt['ds_micro_organismo'].value_counts().reset_index()

    if not coordenadas_filt.empty:

        coordenadas_filt = coordenadas_filt.astype({'latitude': float, 'longitude': float})

        # Mostrando mapa para o usuário
        st.map(data=coordenadas_filt, latitude='latitude', longitude='longitude')

        # Adicionar marcadores para cada unidade (para a opção 'Todos') ou apenas para a unidade específica
        for index, row in coordenadas_filt.iterrows():

            st.markers([(row['latitude'], row['longitude'])], use_container_width=True)

    else:

        st.warning(f'Não há coordenadas disponíveis para a unidade de coleta {ds_unidade_coleta}.')

else:

    st.warning('Por favor, faça o upload dos arquivos (.csv) requisitados.')