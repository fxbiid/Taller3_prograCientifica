from fastapi import APIRouter
from pydantic import BaseModel

from api.cache import cache

router = APIRouter()


class Inicio(BaseModel):
    texto: str
    modelo: int
    longitud: int


@router.post("/generator")
def generar(inicio: Inicio):

    generador = cache.generadores[inicio.modelo]
    texto = generador.generar(inicio.texto,longitud=inicio.longitud)

    return {
        "texto": texto
    }