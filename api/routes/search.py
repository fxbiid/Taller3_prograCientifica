from fastapi import APIRouter
from pydantic import BaseModel

from api.cache import cache

router = APIRouter()


class Consulta(BaseModel):
    consulta: str


@router.post("/search")
def buscar(datos: Consulta):

    resultados = cache.buscador.buscar(
        datos.consulta,
        cache.matriz_tfidf,
        cache.vectorizer,
        cache.preprocessor,
        cache.df
    )

    respuesta = []

    for indice, similitud in resultados:

        fila = cache.df.iloc[indice]

        respuesta.append({

            "libro": fila["n"],

            "capitulo": int(fila["c"]),

            "versiculo": int(fila["v"]),

            "texto": fila["t_x"],

            "similitud": round(similitud, 4)

        })

    return respuesta