import requests
import streamlit as st

API = "http://127.0.0.1:8000"

st.title("Generador de Texto")

inicio = st.text_input(
    "Texto inicial",
    value="in the"
)

if st.button("Generar"):
    respuesta = requests.post(
        f"{API}/generator",

        json={

            "texto": inicio

        }

    )

    texto = respuesta.json()["texto"]
    st.subheader("Texto generado")
    st.write(texto)