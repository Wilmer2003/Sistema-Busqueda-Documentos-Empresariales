# Sistema de Búsqueda y Administración de Documentos Empresariales

**Curso:** Sistemas de Gestión de Bases de Datos (SGBD)  
**Grupo:** 1  
**Proyecto:** Trabajo Final NoSQL  
**Motor NoSQL:** Elasticsearch  
**Estado:** En planificación y configuración inicial.

---

## 1. Descripción del proyecto

El proyecto consiste en desarrollar un sistema web de búsqueda y administración de documentos empresariales utilizando Elasticsearch como motor NoSQL.

El sistema permitirá registrar, indexar, consultar y analizar documentos de diferentes departamentos de una organización, facilitando la búsqueda de información mediante palabras, frases, filtros y consultas de texto completo.

El proyecto busca demostrar el diseño, implementación, administración y evaluación de una solución basada en bases de datos NoSQL.

## 2. Integrantes del equipo

| N.º | Integrante | Responsabilidad |
|---|---|---|
| 1 | SILVA LOPEZ, WILMER ZOILO | Coordinación, GitHub e integración |
| 2 | ALFARO VILLANUEVA, CRISTHIAN ALEJANDRO | Elasticsearch y modelado de datos |
| 3 | URCIA HUAMANCHUMO, JEFFRI AIMAR | Backend y API REST |
| 4 | VENEGAS AGUIRRE, JOSE DAVID | Motor de búsqueda y Query DSL |
| 5 | VERGARA LOPEZ, JUNIOR MANUEL | Frontend e interfaz web |
| 6 | SALINAS CASTRILLON, SEBASTIAN EMMANUEL | Administración, pruebas y rendimiento |

## 3. Tecnologías

| Componente | Tecnología |
|---|---|
| Motor NoSQL | Elasticsearch |
| Backend | Python + FastAPI |
| Frontend | React + Vite |
| Administración | Kibana |
| Contenedores | Docker Compose |
| Comunicación | API REST |
| Control de versiones | Git + GitHub |
| Automatización CI | GitHub Actions |
| Pruebas backend | Pytest |
| Calidad Python | Ruff |
| Pruebas frontend | Vitest |
| Calidad frontend | ESLint |

## 4. Funcionalidades del sistema

El proyecto contempla las siguientes funcionalidades establecidas en el documento de asignación:

1. Registrar documentos empresariales.
2. Indexar información de diferentes departamentos.
3. Realizar búsquedas por palabras y frases.
4. Aplicar filtros por fecha, categoría y responsable.
5. Implementar búsquedas de texto completo.
6. Utilizar agregaciones para generar estadísticas.
7. Gestionar índices, shards y réplicas.

## 5. Arquitectura general

El sistema seguirá las seis capas establecidas en la guía del profesor:

1. **Presentación:** interfaz web desarrollada con React.
2. **API y comunicación:** servicios REST mediante FastAPI.
3. **Lógica de negocio:** procesamiento de las operaciones documentales.
4. **Persistencia NoSQL:** almacenamiento e indexación mediante Elasticsearch.
5. **Distribución y disponibilidad:** configuración de shards, réplicas y mecanismos de disponibilidad según el despliegue.
6. **Administración y monitoreo:** Kibana, índices, seguridad, respaldos y pruebas de rendimiento.

## 6. Estructura del repositorio

```text
sistema-busqueda-documentos-empresariales/
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
│
├── backend/
│   ├── app/
│   │   ├── config/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── pytest.ini
│
├── frontend/
│
├── elasticsearch/
│   ├── mappings/
│   ├── queries/
│   └── scripts/
│
├── docs/
│   ├── informe/
│   ├── diagramas/
│   └── evidencias/
│
├── data/
│   └── sample_documents/
│
├── tests/
│   ├── integration/
│   └── performance/
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## 7. Distribución del desarrollo

| Etapa | Actividad | Responsable |
|---|---|---|
| 1 | Organización y repositorio | Wilmer |
| 2 | Configuración de Elasticsearch | Cristhian |
| 3 | Desarrollo del backend | Jeffri |
| 4 | Consultas y funcionalidades de búsqueda | Jose David |
| 5 | Interfaz web | Junior |
| 6 | Administración y pruebas | Sebastian |
| 7 | Integración general | Todos, coordinados por Wilmer |
| 8 | Documentación y presentación | Todos |

## 8. Plan de trabajo

### Etapa 1. Organización y planificación
- Crear repositorio GitHub.
- Incorporar a los seis integrantes.
- Configurar ramas y protección de main.
- Definir tecnologías.
- Establecer responsabilidades.
- Preparar estructura inicial.

### Etapa 2. Configuración del entorno
- Preparar Docker Compose.
- Levantar Elasticsearch.
- Configurar Kibana.
- Verificar conectividad.
- Documentar el entorno de desarrollo.

### Etapa 3. Modelado e implementación de datos
- Diseñar la estructura de documentos JSON.
- Definir índices y mappings.
- Establecer campos y tipos de datos.
- Configurar índices invertidos y analizadores.
- Definir shards y réplicas.

### Etapa 4. Desarrollo del backend
- Configurar FastAPI.
- Implementar conexión con Elasticsearch.
- Crear endpoints REST.
- Implementar operaciones CRUD.
- Validar las solicitudes.

### Etapa 5. Desarrollo de búsquedas
- Implementar búsquedas por palabras.
- Implementar búsquedas por frases.
- Desarrollar búsquedas de texto completo.
- Agregar filtros.
- Implementar Query DSL y agregaciones.

### Etapa 6. Desarrollo del frontend
- Construir interfaz web.
- Implementar registro de documentos.
- Mostrar resultados.
- Agregar filtros.
- Crear panel de estadísticas.

### Etapa 7. Pruebas y evaluación
- Pruebas funcionales.
- Pruebas de integración.
- Pruebas de rendimiento.
- Medición de latencias.
- Evaluación de índices, shards y réplicas.

### Etapa 8. Documentación y presentación
- Completar el informe técnico.
- Incorporar diagramas.
- Adjuntar evidencias.
- Preparar demostración.
- Revisar los resultados finales.

## 9. Estrategia de Git y GitHub

Se utilizará un flujo de trabajo basado en ramas independientes y Pull Requests.

### Rama principal

`main`

Contendrá únicamente versiones revisadas e integradas del sistema.

### Ramas de trabajo

| Integrante | Rama |
|---|---|
| Wilmer | feature/wilmer-integracion |
| Cristhian | feature/cristhian-elasticsearch |
| Jeffri | feature/jeffri-backend |
| Jose David | feature/jose-busquedas |
| Junior | feature/junior-frontend |
| Sebastian | feature/sebastian-testing |

### Reglas de colaboración

1. Está prohibido realizar cambios directamente en main.
2. Cada integrante trabajará en su propia rama.
3. Antes de comenzar una tarea, deberá actualizar su rama con los cambios de main.
4. Los cambios deberán guardarse mediante commits descriptivos.
5. Todo cambio deberá integrarse mediante Pull Request.
6. Los Pull Requests deberán tener una descripción de los cambios.
7. Se requiere al menos una aprobación de otro integrante.
8. Las pruebas automáticas deberán finalizar correctamente.
9. No se permitirán conflictos pendientes.
10. El coordinador revisará y gestionará las integraciones.

### Flujo de trabajo

```text
main
  |
  |-- feature/wilmer-integracion
  |-- feature/cristhian-elasticsearch
  |-- feature/jeffri-backend
  |-- feature/jose-busquedas
  |-- feature/junior-frontend
  |-- feature/sebastian-testing
         |
         v
    Pull Request
         |
         v
    GitHub Actions
         |
         v
    Revisión y aprobación
         |
         v
    Merge a main
```

## 10. Integración continua (CI)

Se utilizará GitHub Actions para ejecutar automáticamente las validaciones del proyecto.

### Validaciones del backend
- Ruff.
- Pytest.
- Pruebas de código.

### Validaciones del frontend
- ESLint.
- Vitest.
- Compilación con Vite.

### Reglas de integración
- Todos los controles obligatorios deben aprobarse.
- Se requiere revisión de otro integrante.
- Se deben resolver los comentarios pendientes.
- No se permitirá integrar cambios con validaciones fallidas.

Posteriormente se incorporarán pruebas de integración contra Elasticsearch y pruebas de rendimiento.

## 11. Normas de trabajo del equipo

- Mantener comunicación sobre los avances.
- Respetar las responsabilidades asignadas.
- No modificar módulos de otros integrantes sin coordinación.
- Evitar subir archivos innecesarios.
- No subir credenciales ni archivos `.env`.
- Mantener actualizado el repositorio.
- Documentar los cambios importantes.
- Probar las funcionalidades antes de crear un Pull Request.

## 12. Objetivo final

Desarrollar una aplicación web funcional que demuestre el uso de Elasticsearch como motor NoSQL para la búsqueda y administración de documentos empresariales, cumpliendo las funcionalidades y criterios técnicos establecidos por el docente.

---

**Grupo 1 – Sistemas de Gestión de Bases de Datos**
