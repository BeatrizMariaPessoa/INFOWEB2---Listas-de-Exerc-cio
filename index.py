import streamlit as st
from cliente import Cliente, NCliente
import views

tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

with tab1:
    st.header("Cadastre-se como cliente")
    with st.form(key="cadastro"):
        nome = st.text_input('Nome')
        email = st.text_input('Email')
        telefone = st.text_input('Nº de celular')
        botao_inseir = st.form_submit_button("Inserir")
    if botao_inseir:
        views.cliente_inserir(nome, email, telefone)
    for cliente in NCliente.listar():
      st.write(cliente)

with tab3:
    st.header("Atualize seus dados")
    with st.form(key="atualizacao"):
        selecionado = st.selectbox('Qual cliente deseja atualizar os dados?',(NCliente.listar()))
        nome = st.text_input('Nome')
        email = st.text_input('Email')
        telefone = st.text_input('Nº de celular')
        botao_atualizar = st.form_submit_button("Atualizar")
        id = selecionado.Cliente.get_id()
        cliente = Cliente(id, nome, email, telefone)
        if botao_atualizar:
            views.cliente_atualizar(cliente)
