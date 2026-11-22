from datetime import date

from app.schemas.documento import (
    BusquedaOut,
    DocumentoCreate,
    DocumentoOut,
    DocumentoUpdate,
)
from app.services import documento_service as service
from fastapi import APIRouter, HTTPException, Query, status

router = APIRouter(prefix="/api/v1/documentos", tags=["Documentos"])


@router.post("", response_model=DocumentoOut, status_code=status.HTTP_201_CREATED)
def registrar(documento: DocumentoCreate):
    return service.crear(documento.model_dump(mode="json", exclude_none=True))


@router.get("/buscar", response_model=BusquedaOut)
def buscar(
    q: str | None = None,
    categoria: str | None = None,
    departamento: str | None = None,
    responsable: str | None = None,
    tipo_documento: str | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
    pagina: int = Query(1, ge=1),
    tamano: int = Query(10, ge=1, le=100),
):
    return service.buscar(
        q=q,
        categoria=categoria,
        departamento=departamento,
        responsable=responsable,
        tipo_documento=tipo_documento,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta,
        pagina=pagina,
        tamano=tamano,
    )


@router.get("/{doc_id}", response_model=DocumentoOut)
def obtener(doc_id: str):
    doc = service.obtener(doc_id)
    if doc is None:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return doc


@router.put("/{doc_id}", response_model=DocumentoOut)
def actualizar(doc_id: str, cambios: DocumentoUpdate):
    doc = service.actualizar(
        doc_id, cambios.model_dump(mode="json", exclude_none=True)
    )
    if doc is None:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return doc


@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(doc_id: str):
    if not service.eliminar(doc_id):
        raise HTTPException(status_code=404, detail="Documento no encontrado")