import pandas as pd
import streamlit as st
import plotly.express as px

# Header
st.header("Painel de Monitoramento de Resistência Microbiana a Antibióticos")

dados = pd.read_csv("sample_data_clean.csv", sep=",")

# Filtro para selecionar condições de resistência das bactérias (cd_interpretacao_antibiograma)
opcoes_interpretacao = st.multiselect("Selecione as condições de resistência das bactérias:", 
                                      dados["cd_interpretacao_antibiograma"].unique())

# Filtro para selecionar tipos de micro-organismos (ds_micro_organismo)
opcoes_microorganismo = st.multiselect("Selecione os tipos de micro-organismos:", 
                                       dados["ds_micro_organismo"].unique())

# Filtrar o DataFrame com base nas opções selecionadas
dados_filtrados = dados[dados["cd_interpretacao_antibiograma"].isin(opcoes_interpretacao) & 
                        dados["ds_micro_organismo"].isin(opcoes_microorganismo)]

# Exibindo os dados filtrados
st.write("Dados filtrados para o microorganismo e sua resistencia:")
st.write(dados_filtrados)

# Convertendo a coluna 'dh_coleta_exame' para o tipo de dados datetime
dados_filtrados['dh_coleta_exame'] = pd.to_datetime(dados_filtrados['dh_coleta_exame'])

# Agrupando por tempo e contando a ocorrência de cada variável
dados_agrupados = dados_filtrados.groupby(["dh_coleta_exame", "cd_interpretacao_antibiograma", "ds_micro_organismo"]).size().reset_index(name='contagem')

# Verificando se há dados antes de criar o gráfico
if not dados_agrupados.empty:
    # Plotando o gráfico de barras em função do tempo
    fig_barras_tempo = px.bar(dados_agrupados, x="dh_coleta_exame", y="contagem", color="cd_interpretacao_antibiograma", 
                              facet_col="ds_micro_organismo", labels={"contagem": "Contagem", "dh_coleta_exame": "Tempo", "ds_micro_organismo": "Microorganismo", "cd_interpretacao_antibiograma": ""}, 
                              title="Contagem da Resistencia do Microorganismo em função do Tempo")
    st.plotly_chart(fig_barras_tempo)
else:
    st.warning("Não há dados disponíveis para criar o gráfico.")