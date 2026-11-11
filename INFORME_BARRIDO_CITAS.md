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
