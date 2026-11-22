# Consultas Query DSL — Sistema de Búsqueda de Documentos Empresariales

Responsable: Jose David (Búsquedas y Query DSL)
Índice: `documentos_empresariales` (ver `.env.example`)
Mapping de referencia: `elasticsearch/mappings/documentos_mapping.json`

Cada archivo `.json` contiene solo el **cuerpo** de la consulta. Para probarlo en Kibana → Dev Tools:

```
GET documentos_empresariales/_search
{ ...contenido del archivo... }
```

O con curl:

```
curl -X GET "http://localhost:9200/documentos_empresariales/_search" -H "Content-Type: application/json" -d @elasticsearch/queries/01_busqueda_palabra.json
```

## Campos usados (según el mapping)

| Campo | Tipo | Uso en consultas |
|---|---|---|
| titulo | text (spanish) + `.keyword` | búsqueda full-text, orden exacto |
| contenido | text (spanish) | búsqueda por palabra/frase |
| resumen | text (spanish) | búsqueda full-text |
| departamento | keyword | filtro `term`, agregación |
| categoria | keyword | filtro `term`, agregación |
| responsable | text + `.keyword` | búsqueda flexible (`responsable`), filtro exacto/agregación (`responsable.keyword`) |
| tipo_documento | keyword | filtro `term`, agregación |
| etiquetas | keyword | filtro `term`, agregación |
| version | integer | métricas |
| fecha_creacion | date | filtro `range`, histograma |
| fecha_modificacion | date | filtro `range` |

## Catálogo de consultas

| Archivo | Objetivo | Entrada (valores que cambian) | Resultado esperado |
|---|---|---|---|
| 01_busqueda_palabra.json | Buscar documentos que contengan una palabra | `contenido`: palabra | Documentos con esa palabra (o su raíz en español), con fragmentos resaltados |
| 02_busqueda_frase.json | Buscar una frase exacta, en orden | frase en `contenido` y `titulo` | Solo documentos con esa frase; coincidencias en título pesan más |
| 03_fulltext_multicampo.json | Búsqueda de texto completo en varios campos | `query` | Documentos ordenados por relevancia (título x3, resumen x2); tolera errores de tipeo |
| 04_filtro_fecha.json | Filtrar por rango de fechas | `gte`, `lte` | Documentos dentro del rango, del más reciente al más antiguo |
| 05_filtro_categoria_responsable.json | Filtrar por categoría y responsable | `categoria`, `responsable.keyword` | Solo documentos que cumplen ambos filtros |
| 06_busqueda_combinada.json | Texto + todos los filtros + paginación | texto, departamento, categoría, tipo, responsable, fechas, `from`, `size` | Resultados relevantes que respetan todos los filtros |
| 07_agregaciones.json | Estadísticas para mostrar en el sistema | ninguna | Totales por categoría, departamento, tipo, responsable, etiqueta, mes y versión promedio |

## Cómo parametrizarlas desde la API (para Jeffri)

- Los valores del ejemplo (`"contrato"`, `"finanzas"`, `"Juan Perez"`, fechas) son ilustrativos: la API los reemplaza con lo que envíe el usuario.
- En la consulta combinada (06), **cada filtro es opcional**: la API arma la lista `filter` agregando solo los que el usuario envió. Si no hay texto, se omite el bloque `must` y se usa `match_all`.
- `responsable.keyword` es coincidencia exacta (mayúsculas y tildes incluidas). Para una búsqueda flexible por nombre usar `{ "match": { "responsable": "perez" } }`.
- Paginación: `from` = (página - 1) × `size`.
- Fechas en formato ISO (`YYYY-MM-DD`).
- Las agregaciones usan `"size": 0` para devolver solo estadísticas, sin documentos.

## Datos de prueba

Los valores de ejemplo (finanzas, contabilidad, Juan Perez, etc.) deben ajustarse a los datos de prueba reales que cargue Cristhian/Sebastian.
