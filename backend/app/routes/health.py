from app.config.elasticsearch import es_client
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Salud"])


@router.get("/health")
def health():
    if not es_client.ping():
        raise HTTPException(status_code=503, detail="Elasticsearch no disponible")
    return {"estado": "ok", "elasticsearch": "conectado"}