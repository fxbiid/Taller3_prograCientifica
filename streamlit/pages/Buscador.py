import requests
import streamlit as st
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Buscador Semántico")

consulta = st.text_input("Escribe una frase")

if st.button("Buscar"):

    if consulta.strip() == "":
        st.warning("Escribe una consulta.")

    else:
        respuesta = requests.post(

            f"{API}/search",

            json={

                "consulta": consulta

            }

        )

        resultados = respuesta.json()

        if len(resultados) == 0:
            st.warning("No se encontraron resultados.")

        else:
            df = pd.DataFrame(resultados)
            st.dataframe(df,use_container_width=True)