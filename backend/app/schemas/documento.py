from datetime import date

from pydantic import BaseModel, Field


class DocumentoBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=200)
    contenido: str = Field(min_length=1)
    resumen: str | None = None
    departamento: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    responsable: str = Field(min_length=1)
    tipo_documento: str | None = None
    etiquetas: list[str] = []
    version: int = Field(default=1, ge=1)
    fecha_creacion: date = Field(default_factory=date.today)
    fecha_modificacion: date | None = None


class DocumentoCreate(DocumentoBase):
    pass


class DocumentoUpdate(BaseModel):
    titulo: str | None = Field(default=None, min_length=3, max_length=200)
    contenido: str | None = None
    resumen: str | None = None
    departamento: str | None = None
    categoria: str | None = None
    responsable: str | None = None
    tipo_documento: str | None = None
    etiquetas: list[str] | None = None
    version: int | None = Field(default=None, ge=1)


class DocumentoOut(DocumentoBase):
    id: str


class BusquedaOut(BaseModel):
    total: int
    pagina: int
    tamano: int
    resultados: list[DocumentoOut]