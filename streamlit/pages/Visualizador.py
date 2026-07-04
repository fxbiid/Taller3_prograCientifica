import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API = "http://127.0.0.1:8000"

st.title("Vectorización")

col1, col2, col3 = st.columns(3)

with col1:
    modelo = st.selectbox("Modelo",["tfidf", "word2vec"])

with col2:
    dimensiones = st.selectbox("Dimensiones",[2, 3])

with col3:
    limite = st.slider("Cantidad de versículos",50,500,100)

respuesta = requests.get(

    f"{API}/vectorizacion",

    params={

        "modelo": modelo,
        "dimensiones": dimensiones,
        "limite": limite

    }

)

datos = respuesta.json()

df = pd.DataFrame(datos)
if dimensiones == 2:

    fig = px.scatter(df,x="x",y="y",color="libro",hover_data=["testamento","capitulo","versiculo"],title=f"{modelo.upper()} - PCA 2D")

else:
    fig = px.scatter_3d(df,x="x",y="y",z="z",color="libro",hover_data=["testamento","capitulo","versiculo"],title=f"{modelo.upper()} - PCA 3D")

st.plotly_chart(fig,use_container_width=True)