
import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conexão com MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["eshop"]
colecao = db["clientes"]

st.title("CRUD - E-Shop Brasil com MongoDB")

# Inserção
st.subheader("Criar novo cliente")
nome = st.text_input("Nome")
email = st.text_input("Email")
if st.button("Adicionar"):
    if nome and email:
        colecao.insert_one({"nome": nome, "email": email})
        st.success("Cliente adicionado com sucesso!")
    else:
        st.warning("Preencha os campos corretamente.")

# Leitura
st.subheader("Lista de Clientes")
dados = list(colecao.find({}, {"_id": 0}))
df = pd.DataFrame(dados)
st.dataframe(df)

# Atualização
st.subheader("Atualizar cliente")
email_antigo = st.text_input("Email do cliente a atualizar")
novo_nome = st.text_input("Novo nome")
if st.button("Atualizar"):
    resultado = colecao.update_one({"email": email_antigo}, {"$set": {"nome": novo_nome}})
    if resultado.modified_count:
        st.success("Cliente atualizado!")
    else:
        st.info("Nenhum cliente encontrado com esse email.")

# Exclusão
st.subheader("Excluir cliente")
email_excluir = st.text_input("Email do cliente a excluir")
if st.button("Excluir"):
    resultado = colecao.delete_one({"email": email_excluir})
    if resultado.deleted_count:
        st.success("Cliente excluído com sucesso.")
    else:
        st.warning("Cliente não encontrado.")
