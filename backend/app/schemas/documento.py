from datetime import date

from pydantic import BaseModel, Field


class DocumentoBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=200)
    contenido: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    departamento: str = Field(min_length=1)
    responsable: str = Field(min_length=1)
    fecha: date
    etiquetas: list[str] = []


class DocumentoCreate(DocumentoBase):
    pass


class DocumentoUpdate(BaseModel):
    titulo: str | None = Field(default=None, min_length=3, max_length=200)
    contenido: str | None = None
    categoria: str | None = None
    departamento: str | None = None
    responsable: str | None = None
    fecha: date | None = None
    etiquetas: list[str] | None = None


class DocumentoOut(DocumentoBase):
    id: str


class BusquedaOut(BaseModel):
    total: int
    pagina: int
    tamano: int
    resultados: list[DocumentoOut]