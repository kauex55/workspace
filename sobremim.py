import streamlit as st
import datetime as dt

st.title("Sobre mim")


st.subheader("Nome")
nome = st.text_input("Qual é o seu nome?")
st.write("Olá, ", nome)

st.subheader("Idade")
idade = st.slider("Selecione sua idade", 0, 100)
st.write("Sua idade é", idade)


st.subheader("Gênero")
genero = st.radio(
    "Qual seu gênero?",
    ('Masculino', 'Feminino'))

st.write("Você selecionou:", genero)

st.subheader("Data de nascimento")
d = st.date_input(
    "Qual sua data de nascimento?",
    dt.date(2019, 7, 6))
st.write('Sua data de nascimento é:', d)

st.subheader("Cor favorita")

cor = st.color_picker('Selecione uma cor', '#00f900')
st.write('Sua cor favorita é', cor)

