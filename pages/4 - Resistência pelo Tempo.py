import pandas as pd
import streamlit as st
import time as tm

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
        paleta_cor = None  # Se 'Todos', não é necessário paleta de cores
    else:
        arquivo_filt = arquivo[arquivo['ds_micro_organismo'] == ds_micro_organismo]
        paleta_cor = None  # Não está claro o que você quer fazer com paleta_cor aqui

    arquivo['dh_admissao_paciente'] = pd.to_datatime(arquivo['dh_admissao_paciente'])

    # Corrigindo a contagem de resistências
    cont_res = arquivo_filt[arquivo_filt['cd_interpretacao_antibiograma'] == 'Resistente'].groupby(arquivo['dh_admissao_paciente']).size().reset_index(name='count')

    # Mostrando o gráfico para o usuário
    st.text('Resistência pelo Tempo')
    st.line_chart(
        data=cont_res,
        x=arquivo['dh_admissao_paciente'], 
        y="count",
        color=paleta_cor
    )