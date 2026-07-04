from codigo.bibliaDataset import BibliaDataset
from collections import Counter
from codigo.textPreprocesamiento import TextPreprocesamiento

def cargar_biblia():

    biblia = BibliaDataset(
        "data/t_kjv.csv",
        "data/key_english.csv"
    )

    return biblia.load_data()


def filtrar_biblia(df, testamento=None, libro=None, capitulo=None):
    if testamento:
        df = df[df["t_y"] == testamento]

    if libro:
        df = df[df["n"] == libro]

    if capitulo:
        df = df[df["c"] == capitulo]

    return df

def cantidad_por_libro(df):

    return (
        df.groupby("n")
        .size()
        .sort_values(ascending=False)
        .to_dict()
    )

def promedio_por_libro(df):

    copia = df.copy()

    copia["largo"] = copia["t_x"].str.len()

    return (
        copia.groupby("n")["largo"]
        .mean()
        .round(2)
        .to_dict()
    )


def obtener_top_palabras(df, cantidad=20):
    pre = TextPreprocesamiento()
    contador = Counter()

    for texto in df["t_x"]:
        tokens = pre.preprocess(str(texto))
        contador.update(tokens)

    resultado = []

    for palabra, frecuencia in contador.most_common(cantidad):
        resultado.append({"palabra": palabra,"frecuencia": frecuencia})

    return resultado

def obtener_frecuencias(df):

    pre = TextPreprocesamiento()

    contador = Counter()

    for texto in df["t_x"]:

        tokens = pre.preprocess(str(texto))

        contador.update(tokens)

    return dict(contador)