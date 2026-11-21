# Documentación del backend (API REST)

Esta es la documentación de la API que desarrollé con FastAPI. Sirve para que el resto del equipo, sobre todo Junior con el frontend, sepa qué direcciones tiene la API y qué datos enviar y recibir. También se puede ver y probar en http://127.0.0.1:8000/docs cuando la API está encendida.

**Importante:** los campos del documento son provisionales. Los voy a ajustar cuando Cristhian publique el modelo JSON y el mapping definitivos.

## Cómo encender la API

    cd backend
    .\.venv\Scripts\Activate.ps1
    uvicorn app.main:app --reload

La API queda en http://127.0.0.1:8000

## Endpoints que hice

| Método | Ruta | Para qué sirve |
|---|---|---|
| GET | /health | Comprueba si la API está conectada con Elasticsearch |
| POST | /api/v1/documentos | Registra un documento nuevo |
| GET | /api/v1/documentos/buscar | Busca documentos con filtros |
| GET | /api/v1/documentos/{id} | Trae un documento por su id |
| PUT | /api/v1/documentos/{id} | Actualiza los campos que se envíen |
| DELETE | /api/v1/documentos/{id} | Elimina un documento |

## Campos de un documento

| Campo | Tipo | Obligatorio | Regla |
|---|---|---|---|
| titulo | texto | Sí | Entre 3 y 200 caracteres |
| contenido | texto | Sí | No puede estar vacío |
| categoria | texto | Sí | No puede estar vacío |
| departamento | texto | Sí | No puede estar vacío |
| responsable | texto | Sí | No puede estar vacío |
| fecha | fecha | Sí | Formato AAAA-MM-DD |
| etiquetas | lista de textos | No | Si no se envía, queda vacía |

## Ejemplos

### Registrar un documento (POST /api/v1/documentos)

Lo que se envía:

    {
      "titulo": "Política de vacaciones 2026",
      "contenido": "Los empleados tienen derecho a 30 días de vacaciones al año.",
      "categoria": "Políticas",
      "departamento": "Recursos Humanos",
      "responsable": "Ana Torres",
      "fecha": "2026-03-15",
      "etiquetas": ["vacaciones", "rrhh"]
    }

Lo que responde (código 201). Es el mismo documento más el id que le asigna Elasticsearch:

    {
      "id": "abc123",
      "titulo": "Política de vacaciones 2026",
      "contenido": "Los empleados tienen derecho a 30 días de vacaciones al año.",
      "categoria": "Políticas",
      "departamento": "Recursos Humanos",
      "responsable": "Ana Torres",
      "fecha": "2026-03-15",
      "etiquetas": ["vacaciones", "rrhh"]
    }

### Buscar documentos (GET /api/v1/documentos/buscar)

Todos los parámetros son opcionales y se pueden combinar:

| Parámetro | Qué hace |
|---|---|
| q | Busca el texto en el título y en el contenido |
| categoria | Filtra por categoría |
| responsable | Filtra por responsable |
| fecha_desde | Fecha mínima (AAAA-MM-DD) |
| fecha_hasta | Fecha máxima (AAAA-MM-DD) |
| pagina | Número de página, empieza en 1 (por defecto 1) |
| tamano | Resultados por página, de 1 a 100 (por defecto 10) |

Ejemplo de búsqueda:

    GET /api/v1/documentos/buscar?q=vacaciones&categoria=Políticas&fecha_desde=2026-01-01&pagina=1&tamano=10

Lo que responde (código 200):

    {
      "total": 1,
      "pagina": 1,
      "tamano": 10,
      "resultados": [
        {
          "id": "abc123",
          "titulo": "Política de vacaciones 2026",
          "contenido": "Los empleados tienen derecho a 30 días de vacaciones al año.",
          "categoria": "Políticas",
          "departamento": "Recursos Humanos",
          "responsable": "Ana Torres",
          "fecha": "2026-03-15",
          "etiquetas": ["vacaciones", "rrhh"]
        }
      ]
    }

Si no encuentra nada, responde con "total": 0 y "resultados": []. El frontend debe mostrar el estado vacío.

### Ver un documento (GET /api/v1/documentos/{id})

Responde (código 200) con el documento completo, igual que en el registro.

### Actualizar un documento (PUT /api/v1/documentos/{id})

Solo se envían los campos que se quieren cambiar:

    { "categoria": "Normativas" }

Responde (código 200) con el documento completo