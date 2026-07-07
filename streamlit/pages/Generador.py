import requests
import streamlit as st

API = "http://127.0.0.1:8000"

st.title("Generador de Texto")

modelo = st.selectbox(
    "Modelo",
    ["Unigrama", "Bigrama", "Trigrama"]
)

inicio = st.text_input("Texto inicial",value="in the")

longitud = st.slider(
    "Longitud máxima",
    min_value=10,
    max_value=100,
    value=30
)

if st.button("Generar"):

    valor_modelo = {
        "Unigrama": 1,
        "Bigrama": 2,
        "Trigrama": 3
    }[modelo]

    respuesta = requests.post(
        f"{API}/generator",
        json={
            "texto": inicio,
            "modelo": valor_modelo,
            "longitud": longitud
        }
    )

    texto = respuesta.json()["texto"]
    st.subheader("Texto generado")
    st.write(texto)