from fastapi import APIRouter
from api.services import (
    cargar_biblia,
    filtrar_biblia,
    cantidad_por_libro,
    promedio_por_libro,
    obtener_top_palabras,
    obtener_frecuencias
)

router = APIRouter()


@router.get("/dashboard")
def dashboard(
        testamento: str = None,
        libro: str = None,
        capitulo: int = None
):

    df = cargar_biblia()

    df = filtrar_biblia(df, testamento, libro, capitulo)

    return {

        "cantidad_versiculos": len(df),

        "largo_promedio":
            round(df["t_x"].str.len().mean(), 2),

        "versiculos_por_libro":
            cantidad_por_libro(df),

        "promedio_por_libro":
            promedio_por_libro(df),

        "top_palabras":
            obtener_top_palabras(df)

    }
@router.get("/filters")
def filtros():

    df = cargar_biblia()

    return {
        "testamentos": sorted(df["t_y"].unique().tolist()),
        "libros": sorted(df["n"].unique().tolist()),
        "capitulos": sorted(df["c"].unique().tolist())
    }

@router.get("/dashboard/versiculos-por-libro")
def versiculos_por_libro(
        testamento: str = None,
        libro: str = None,
        capitulo: int = None
):

    df = cargar_biblia()

    df = filtrar_biblia(
        df,
        testamento,
        libro,
        capitulo
    )

    resultado = (
        df.groupby("n")
        .size()
        .reset_index(name="cantidad")
        .sort_values("cantidad", ascending=False)
    )

    return resultado.to_dict(orient="records")

@router.get("/dashboard/promedio-por-libro")
def promedio_libro(
        testamento: str = None,
        libro: str = None,
        capitulo: int = None
):

    df = cargar_biblia()

    df = filtrar_biblia(
        df,
        testamento,
        libro,
        capitulo
    )

    df["largo"] = df["t_x"].str.len()

    resultado = (
        df.groupby("n")["largo"]
        .mean()
        .round(2)
        .reset_index(name="promedio")
        .sort_values("promedio", ascending=False)
    )

    return resultado.to_dict(orient="records")

@router.get("/dashboard/top-palabras")
def top_palabras(
        testamento: str = None,
        libro: str = None,
        capitulo: int = None
):

    df = cargar_biblia()

    df = filtrar_biblia(
        df,
        testamento,
        libro,
        capitulo
    )

    return obtener_top_palabras(df)

@router.get("/dashboard/frecuencias")
def frecuencias(
        testamento: str = None,
        libro: str = None,
        capitulo: int = None
):

    df = cargar_biblia()

    df = filtrar_biblia(
        df,
        testamento,
        libro,
        capitulo
    )

    return obtener_frecuencias(df)