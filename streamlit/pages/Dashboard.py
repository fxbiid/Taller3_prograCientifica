import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

API = "http://127.0.0.1:8000"

st.title("Dashboard")


filtros = requests.get(f"{API}/filters").json()

col1, col2, col3 = st.columns(3)

with col1:
    testamento = st.selectbox(
        "Testamento",
        [""] + filtros["testamentos"]
    )

with col2:
    libro = st.selectbox(
        "Libro",
        [""] + filtros["libros"]
    )

with col3:
    capitulo = st.selectbox(
        "Capítulo",
        [""] + filtros["capitulos"]
    )

params = {}

if testamento:
    params["testamento"] = testamento

if libro:
    params["libro"] = libro

if capitulo:
    params["capitulo"] = capitulo


dashboard = requests.get(
    f"{API}/dashboard",
    params=params
).json()

m1, m2 = st.columns(2)

with m1:
    st.metric(
        "Versículos",
        dashboard["cantidad_versiculos"]
    )

with m2:
    st.metric(
        "Largo promedio",
        dashboard["largo_promedio"]
    )

datos = requests.get(
    f"{API}/dashboard/versiculos-por-libro",
    params=params
).json()

df = pd.DataFrame(datos)

fig = px.bar(
    df,
    x="n",
    y="cantidad",
    title="Cantidad de versículos por libro"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

datos = requests.get(
    f"{API}/dashboard/promedio-por-libro",
    params=params
).json()

df = pd.DataFrame(datos)

fig = px.bar(
    df,
    x="n",
    y="promedio",
    title="Longitud promedio por libro"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

frecuencias = requests.get(
    f"{API}/dashboard/frecuencias",
    params=params
).json()

wordcloud = WordCloud(
    width=900,
    height=400,
    background_color="white"
).generate_from_frequencies(frecuencias)

fig, ax = plt.subplots(figsize=(12, 6))

ax.imshow(wordcloud)

ax.axis("off")

st.pyplot(fig)