import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página Streamlit
st.set_page_config(page_title = 'Resistência em Função do Tempo', page_icon = '🦠', initial_sidebar_state = 'collapsed')

# Cabeçalho da aplicação
st.header('Painel de Monitoramento Microbiológico')

# Carregamento dos dados a partir de um arquivo CSV
dados = pd.read_csv("sample_data_clean.csv", sep = ",")

# Subcabeçalho
st.subheader('Resistência em Função do Tempo', divider = 'rainbow')

# Filtro para selecionar tipos de microrganismos (ds_micro_organismo)
opcoes_microorganismo = st.multiselect('Selecione os tipos de microrganismos:', dados['ds_micro_organismo'].unique())

# Filtro para selecionar condições de resistência das bactérias (cd_interpretacao_antibiograma)
opcoes_interpretacao = st.multiselect('Selecione as condições de resistência dos microrganismos:',
                                      dados['cd_interpretacao_antibiograma'].unique())

# Filtrar o DataFrame com base nas opções selecionadas
dados_filt = dados[dados['ds_micro_organismo'].isin(opcoes_microorganismo) &
                        dados['cd_interpretacao_antibiograma'].isin(opcoes_interpretacao)]

# Exibindo os dados filtrados
st.write('Dados filtrados para o microrganismo e sua resistência:')
st.write(dados_filt)

# Convertendo a coluna 'dh_coleta_exame' para o tipo de dados datetime
dados_filt['dh_coleta_exame'] = pd.to_datetime(dados_filt['dh_coleta_exame'])

# Agrupando por tempo e contando a ocorrência de cada variável
dados_agrupados = dados_filt.groupby(['dh_coleta_exame', 'cd_interpretacao_antibiograma',
                                      'ds_micro_organismo']).size().reset_index(name = 'contagem')

# Verificando se há dados antes de criar o gráfico
if dados_agrupados.empty:

    st.warning('Não há dados disponíveis para criar o gráfico.')

else:

    # Plotando o gráfico de barras em função do tempo
    fig_barras_tempo = px.bar(dados_agrupados, x = "dh_coleta_exame", y = "contagem", color = "cd_interpretacao_antibiograma",
                              facet_col = "ds_micro_organismo", labels = {"contagem": "Contagem", "dh_coleta_exame": "Tempo",
                                                                          "ds_micro_organismo": "Microrganismo",
                                                                          "cd_interpretacao_antibiograma": ""},
                              title = "Contagem da Resistência do Microrganismo em Função do Tempo")

    st.plotly_chart(fig_barras_tempo)
