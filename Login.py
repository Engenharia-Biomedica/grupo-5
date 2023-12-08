from PIL import Image
import streamlit as st

# Configuração da página Streamlit
st.set_page_config(page_title = 'Login', page_icon = '🦠', initial_sidebar_state = 'collapsed')

# Cabeçalho da aplicação
st.header('Painel de Monitoramento Microbiológico')

# Carregando imagem para o logo
logo = Image.open('logo_pbl2.png')

# Dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col = st.columns(3)

# Colocando o logo na coluna central
with cent_col:

    st.image(logo, width = 200)

# Credenciais de login
credenciais_corretas = {'usuario': '123', 'senha': '456'}

# Área de login
login = st.text_input('Usuário')
senha = st.text_input('Senha', type = 'password')

# Verifica se as credenciais estão corretas ao pressionar o botão de login
if st.button('Login'):

    # Verifica se as credenciais inseridas são válidas
    if login == credenciais_corretas['usuario'] and senha == credenciais_corretas['senha']:

        st.success('Login bem-sucedido!')

    else:

        st.error('Credenciais incorretas. Tente novamente.')

else:

    # Se não houver login realizado
    st.warning('Faça o login para acessar os dados.')
