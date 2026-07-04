from fastapi import FastAPI
from api.routes.dashboard import router as dashboard_router
from api.routes.search import router as search_router
app = FastAPI(
    title="Bible API"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


app.include_router(dashboard_router)
app.include_router(search_router)