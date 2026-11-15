# Informe del bloque de bibliografía — rama `review`

**Fecha:** 2026-11-08
**Base:** `main.pdf` 79 páginas · 756 337 B · `e5ce55fd…`
**Herramienta:** `verificar_dois.py` (CrossRef / DataCite) + resolución individual de los casos dudosos
**Alcance:** las 52 entradas de `TuArchivo.bib`, todas citadas en el manuscrito (52 citadas / 52 entradas, 0 huérfanas).

## 1. Resultado de la verificación automática

| Estado | Entradas |
|---|---|
| `OK` — DOI resuelve y metadata coincide | **44** |
| `SIN DOI` | 5 |
| `AUTOR NO COINCIDE` | 2 |
| `TITULO PARCIAL` (artefacto MathML, no defecto real) | 1 |

Duplicados por título normalizado: **ninguno**.

Las cinco entradas sin DOI se resolvieron una por una:

| Clave | Qué es | Veredicto |
|---|---|---|
| `Glover2017` | libro, *Power System Analysis and Design* | legítimo sin DOI (ISBN 9781305632134 verificado) |
| `Saadat2010` | libro, *Power System Analysis* | legítimo sin DOI |
| `Machuca2017` | tesis de maestría, Universidad Nacional de Colombia | **verificada en el repositorio UNAL** (handle 62236) |
| `Guo2026` | preprint arXiv 2604.03958 | **verificado en arXiv**, DOI añadido |
| `Gupta2026` | nota de prensa de SolarQuarter | URL viva (HTTP 200); fuente no revisada por pares |

## 2. Hallazgos y correcciones

### B1 · `DiFazio2024Linear` — rango de páginas equivocado · **CORREGIDO**
El `.bib` declaraba `4749--4759`; CrossRef devuelve `4749-4761`. Corregido.

### B2 · `Fathima2024` — nombres de autor desordenados · **CORREGIDO**
El registro del editor invierte los componentes (`family=L`, `given=Premalatha`), y el `.bib` los había trasladado tal cual. Normalizado a `Fathima, S. Faazila and Premalatha, L. and Yuvaraj, Prithviraj`, de modo que la cita se lee «Fathima et al.» y el segundo autor conserva su nombre.

### B3 · `Guo2026` — preprint sin identificador · **CORREGIDO**
Añadido `doi={10.48550/arXiv.2604.03958}`, que resuelve a `arxiv.org/abs/2604.03958` (HTTP 200). Autores y título coinciden con la entrada.

### B4 · `Machuca2017` — autora incompleta y sin localizador · **CORREGIDO**
El repositorio de la Universidad Nacional registra «Machuca Moreno, **Laura Alejandra**» y el título exacto. Se completó el nombre y se añadieron `type` y `url` con el handle. La entrada deja de ser opaca: se puede abrir.

### B5 · `Gupta2026` — nota de prensa como fuente de una cifra · **ABIERTO**
Sostiene el dato de capacidad renovable instalada. La URL responde, pero es una nota de prensa, no una fuente primaria. Opciones: mantenerla declarando `howpublished` (ya está) o sustituirla por el informe primario de IRENA/RE Statistics, que es lo que la nota resume. Decisión del autor.

### B6 · `Liu2024` — la clave dice 2024 y la entrada es de 2023 · **COSMÉTICO**
El DOI `10.1016/j.ijepes.2022.108679` corresponde a 2023, vol. 145, y la entrada declara `year={2023}`, correcto. Solo la etiqueta de la clave quedó desfasada; renombrarla obliga a tocar las citas del texto y no aporta nada verificable.

## 3. Verificación de la compilación

Tras las correcciones, reconstrucción desde cero (`latexmk -C` + `latexmk -pdf`): **79 páginas · 756 337 B · `e5ce55fd…`**, 0 errores, 0 citas indefinidas, 1 overfull preexistente (`TEORIA`), **0 avisos de BibTeX** y sin `??`. En el PDF se leen `Fathima et al.`, `Machuca Moreno, 2017`, `Guo et al.` y el rango `4749–4761`.

Respaldo previo del `.bib`: `TuArchivo.bib.bak_20261110_bib`.

## 4. Lo que queda para el autor

- **B5**: decidir si la cifra de capacidad renovable se sostiene con la nota de prensa o con el informe primario.
- Revisión de pertinencia: varias entradas del `.bib` se citan para afirmaciones genéricas de contexto. Eso no se detecta con CrossRef —requiere leer la frase y preguntar si la fuente dice lo que se le atribuye—, y es la clase de defecto que ya apareció dos veces en la introducción (Gomes/Liu y la frase de MQTT, H16).
