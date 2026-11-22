from app.config.settings import settings
from app.routes import documentos, health
from elastic_transport import ConnectionError as ESConnectionError
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title="Sistema de Búsqueda de Documentos Empresariales")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",")],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ESConnectionError)
async def elasticsearch_caido(request: Request, exc: ESConnectionError):
    return JSONResponse(
        status_code=503,
        content={"detail": "No se pudo conectar con Elasticsearch"},
    )


app.include_router(health.router)
app.include_router(documentos.router)