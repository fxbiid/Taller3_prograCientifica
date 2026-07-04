from fastapi import FastAPI
from api.routes.dashboard import router as dashboard_router
from api.routes.search import router as search_router
from api.routes.pca import router as pca_router
from api.routes.generator import router as generator_router
Inicio = FastAPI(
    title="Bible API"
)


@Inicio.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


Inicio.include_router(dashboard_router)
Inicio.include_router(search_router)

Inicio.include_router(pca_router)
Inicio.include_router(generator_router)