from fastapi import FastAPI

from api.routes.dashboard import router as dashboard_router

app = FastAPI(
    title="Bible API"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


app.include_router(dashboard_router)