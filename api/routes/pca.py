from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from api.cache import cache

router = APIRouter()


@router.get("/vectorizacion")
def obtener_vectorizacion(
        modelo: str = "tfidf",
        dimensiones: int = 2,
        limite: int = 100
):
        if modelo.lower() == "tfidf":

            if dimensiones == 3:
                componentes = cache.pca3d
            else:
                componentes = cache.pca2d

        elif modelo.lower() == "word2vec":

            if dimensiones == 3:
                componentes = cache.word2vec_pca3d
            else:
                componentes = cache.word2vec_pca2d

        else:

            raise HTTPException(
                status_code=400,
                detail="Modelo no disponible."
            )


        resultado = []

        for i, fila in cache.df.head(limite).iterrows():

            punto = {

                "libro": fila["n"],

                "testamento": fila["t_y"],

                "capitulo": int(fila["c"]),

                "versiculo": int(fila["v"]),

                "x": float(componentes[i][0]),

                "y": float(componentes[i][1])

            }

            if dimensiones == 3:
                punto["z"] = float(componentes[i][2])

            resultado.append(punto)

        return resultado