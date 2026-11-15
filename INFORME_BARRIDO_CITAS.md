# Barrido transversal de citas vigiladas

**Fecha:** 2026-11-08 · tras aplicar el lote 4
**Objeto:** verificar que los defectos corregidos por frase no sobreviven en otras secciones, revisando **cada aparición** de las cinco claves problemáticas.

## Reparaciones del lote 4 aplicadas

| ID | Cambio |
|---|---|
| C1 | `AlvarezLopez2026` retirada de `DISENO` (clúster) y de `IMPLEMENTACION` (red Ethernet) |
| C2 | `Barzegari2022Resilient` retirada de la lista de métricas de la actividad 4.3 |
| C3 | `Alam2024` → `Saadat2010` en el generador diésel de `IMPLEMENTACION` |
| C4 | `Zhang2024` y `Zhao2025` retiradas de la política de edad del dato |
| P1 | `Gomes2022FMI30` retirada de los temporizadores ZeroMQ de `DISENO` |
| P2 | «teorema de consistencia numérica» → «análisis de error de acoplamiento explícito» |

## Barrido: 16 apariciones revisadas

| Sitio | Frase | Veredicto |
|---|---|---|
| `ANTECEDENTES:9` | consenso data-driven tolerante a fallos | correcta |
| `ANTECEDENTES:40` | arquitecturas en el borde (Edge/IoT) | correcta |
| `ANTECEDENTES:47` | observadores y aislamiento de enlaces | correcta |
| `ANTECEDENTES:52` | paradigma de co-simulación | correcta |
| `ANTECEDENTES:61` | nodo slack y convertidores de interconexión | correcta |
| `DISENO:17` | cinco tipologías, generador diésel gobernado | **corregida en el barrido**: `Alam2024` → `Saadat2010` |
| `IMPLEMENTACION:95` | corriente límite del PV frente a temperatura | parcial aceptada: la revisión de integración de renovables cubre el modelo fotovoltaico |
| `INTRODUCCION:10` | agentes en el borde coordinando con vecinos | correcta |
| `INTRODUCCION:12` | plataforma de co-simulación multitasa | correcta |
| `JUSTIFICACION:7` | márgenes de robustez ante retardos | correcta |
| `JUSTIFICACION:10` | co-simulación acoplada | correcta |
| `JUSTIFICACION:16` | madurez tecnológica CHIL | parcial aceptada |
| `PROBLEMA:26` | latencia y pérdida en dispositivos del borde | parcial aceptada |
| `PROBLEMA:30` | metodología de co-simulación requerida | correcta |
| `PROBLEMA:30` | evaluación de resiliencia del consenso | correcta |

**Resultado:** una corrección nueva encontrada por el barrido y ninguna supervivencia de los defectos ya reparados.

## Efecto en el `.bib`

Al retirar `Zhang2024` de su último sitio quedó huérfana y salió del `.bib`: **49 entradas**, todas citadas.

## Verificación

`latexmk -C` + `latexmk -pdf`: **78 páginas · 753 698 B · `fffd1075…`**, 0 errores de compilación, 0 citas indefinidas, 0 avisos de BibTeX, sin `??`. Auditoría de referencias: **49 citadas / 49 entradas**, ninguna huérfana en ningún sentido.

## Cierre del bloque de pertinencia

100 instancias revisadas en cuatro lotes y 16 apariciones en el barrido: **11 citas no pertinentes retiradas o sustituidas**, **17 parciales** documentadas y **tres referencias eliminadas** del `.bib` (`Verma2024`, `Wang2022DataDriven`, `Zhang2024`), de 52 a 49.

La regla que deja este bloque: una cita se corrige sobre la **clave**, no sobre la frase; de lo contrario reaparece dos capítulos más abajo con el mismo defecto.

## Las dos parciales aceptadas, revisadas a fondo (2026-11-08)

### `IMPLEMENTACION.tex:95` — no era una cita débil, era un error de contenido

La frase atribuía al BESS «saturación dinámica de corriente límite en función de la **temperatura de celda**». El código (`BESS/SistemaBESS.py`) no contiene ninguna lógica térmica: el límite de corriente depende de la **tensión en el punto de conexión**, con una rampa de `_current_limit_dynamic` entre 0,85 y 0,50 p.u. y un factor independiente de LVRT con umbrales en 0,88 y 0,50 p.u.

La descripción además omitía el techo de absorción: el confinamiento es **asimétrico** — 0,20 a 0,90 para descarga, hasta 0,95 para carga —, justo el límite que interviene en el régimen excedentario del capítulo 8.

*Reescrita* según el código y sin cita: la lógica está en el archivo y no requiere respaldo externo.

### `JUSTIFICACION.tex:16` — autoevaluación con respaldo ajeno

La madurez CHIL del banco es una afirmación sobre el propio trabajo; `Diaz2025` y `AlvarezLopez2026` no pueden respaldarla. Cita retirada; el aporte queda declarado como propio. Ambas claves siguen citadas en otros sitios.

### Verificación

**78 páginas · 753 887 B · `2c4c8c38…`**, 0 errores, 0 citas indefinidas, 0 avisos de BibTeX, sin `??`; **49 citadas / 49 entradas**.
