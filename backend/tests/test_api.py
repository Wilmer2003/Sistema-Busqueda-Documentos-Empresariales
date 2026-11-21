from app.main import app
from app.services import documento_service
from fastapi.testclient import TestClient

client = TestClient(app)

DOCUMENTO_VALIDO = {
    "titulo": "Manual de ventas",
    "contenido": "Texto de prueba",
    "categoria": "Manuales",
    "departamento": "Ventas",
    "responsable": "Luis Perez",
    "fecha": "2026-01-10",
}


def test_registro_invalido_devuelve_422():
    respuesta = client.post("/api/v1/documentos", json={"titulo": "ab"})
    assert respuesta.status_code == 422


def test_registro_valido_devuelve_201(monkeypatch):
    monkeypatch.setattr(
        documento_service, "crear", lambda data: {"id": "1", **data}
    )
    respuesta = client.post("/api/v1/documentos", json=DOCUMENTO_VALIDO)
    assert respuesta.status_code == 201
    assert respuesta.json()["id"] == "1"


def test_documento_inexistente_devuelve_404(monkeypatch):
    monkeypatch.setattr(documento_service, "obtener", lambda doc_id: None)
    respuesta = client.get("/api/v1/documentos/no-existe")
    assert respuesta.status_code == 404