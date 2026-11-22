from datetime import date

from app.config.elasticsearch import es_client
from app.config.settings import settings

from elasticsearch import NotFoundError

INDEX = settings.elasticsearch_index


def _a_salida(hit: dict) -> dict:
    return {"id": hit["_id"], **hit["_source"]}


def crear(data: dict) -> dict:
    if not data.get("fecha_modificacion"):
        data["fecha_modificacion"] = data["fecha_creacion"]
    resp = es_client.index(index=INDEX, document=data, refresh="wait_for")
    return {"id": resp["_id"], **data}


def obtener(doc_id: str) -> dict | None:
    try:
        resp = es_client.get(index=INDEX, id=doc_id)
    except NotFoundError:
        return None
    return _a_salida(resp)


def actualizar(doc_id: str, cambios: dict) -> dict | None:
    cambios["fecha_modificacion"] = date.today().isoformat()
    try:
        es_client.update(index=INDEX, id=doc_id, doc=cambios, refresh="wait_for")
    except NotFoundError:
        return None
    return obtener(doc_id)


def eliminar(doc_id: str) -> bool:
    try:
        es_client.delete(index=INDEX, id=doc_id, refresh="wait_for")
    except NotFoundError:
        return False
    return True


def buscar(
    q: str | None,
    categoria: str | None,
    departamento: str | None,
    responsable: str | None,
    tipo_documento: str | None,
    fecha_desde: date | None,
    fecha_hasta: date | None,
    pagina: int,
    tamano: int,
) -> dict:
    must = []
    filtros = []

    if q:
        must.append(
            {"multi_match": {"query": q, "fields": ["titulo^2", "resumen", "contenido"]}}
        )
    if categoria:
        filtros.append({"term": {"categoria": categoria}})
    if departamento:
        filtros.append({"term": {"departamento": departamento}})
    if responsable:
        filtros.append({"term": {"responsable.keyword": responsable}})
    if tipo_documento:
        filtros.append({"term": {"tipo_documento": tipo_documento}})
    if fecha_desde or fecha_hasta:
        rango = {}
        if fecha_desde:
            rango["gte"] = fecha_desde.isoformat()
        if fecha_hasta:
            rango["lte"] = fecha_hasta.isoformat()
        filtros.append({"range": {"fecha_creacion": rango}})

    query = {"bool": {"must": must or [{"match_all": {}}], "filter": filtros}}
    resp = es_client.search(
        index=INDEX, query=query, from_=(pagina - 1) * tamano, size=tamano
    )
    return {
        "total": resp["hits"]["total"]["value"],
        "pagina": pagina,
        "tamano": tamano,
        "resultados": [_a_salida(h) for h in resp["hits"]["hits"]],
    }