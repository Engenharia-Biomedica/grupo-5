import streamlit as st

# Credenciais de login
credenciais_corretas = {'usuario': '123', 'senha': '456'}

# Área de login
login = st.text_input('Usuário')
senha = st.text_input('Senha', type='password')

# Verifica se as credenciais estão corretas ao pressionar o botão de login
if st.button('Login'):

    if login == credenciais_corretas['usuario'] and senha == credenciais_corretas['senha']:

        st.success('Login bem-sucedido!')

    else:

        st.error('Credenciais incorretas. Tente novamente.')

# Se não houver login realizado, encerra o script
else:

    st.warning('Faça o login para acessar os dados.')
    st.stop()