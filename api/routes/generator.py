from fastapi import APIRouter
from pydantic import BaseModel

from api.cache import cache

router = APIRouter()


class Inicio(BaseModel):
    texto: str


@router.post("/generator")
def generar(inicio: Inicio):

    texto = cache.generador.generar(inicio.texto,longitud=30)

    return {
        "texto": texto
    }