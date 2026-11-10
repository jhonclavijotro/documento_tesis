# Informe de coherencia estructural — rama `review`

**Fecha:** 2026-11-08
**Base:** commit `ef23326` · `main.pdf` 79 páginas · 751 023 B · `6ff311dc…`
**Herramientas:** `coherencia_tesis.py`, `auditar_referencias.py`, `auditoria_estructural(2).py`
**Alcance:** estructura del documento completo (portada, introducción y ocho secciones numeradas).

## 1. Métricas de partida

| Control | Resultado |
|---|---|
| Archivos incluidos en `main.tex` | 10, todos existentes; ninguno huérfano en `SECCIONES/` |
| Secciones numeradas | 8 (`PROBLEMA` … `RESULTADOS`); la introducción declara «ocho» y enumera 8 ítems — **coincide** |
| Referencias cruzadas sin definir | 0 |
| Etiquetas duplicadas | 0 |
| Figuras | 9, todas citadas desde el texto |
| Tablas | 5 (I–V: 1 en Antecedentes, 4 en Resultados), todas citadas |
| Estilo de cita | uniforme: `Figura~\ref`, `Tabla~\ref`, `Las Figuras~\ref{a} y~\ref{b}` |
| Bibliografía | 52 citadas / 52 entradas; 0 huérfanas en ambos sentidos |
| Frases idénticas en más de una sección | 0 (no hay copia-pega entre capítulos) |

La estructura formal está sana. Los hallazgos son de **contenido que no concuerda con su envoltorio**, no de mecánica de LaTeX.

---

## 2. Hallazgos

### H7 · [Alto] El resumen de la portada describe otro sistema — **CORREGIDO (2026-11-08)**

`SECCIONES/PORTADA.tex:45-51`. El resumen afirmaba que el entorno «generará las respuestas dinámicas del sistema y las transmitirá en tiempo real utilizando el protocolo de mensajería ligero **MQTT**», y las palabras clave incluían **MQTT**.

*Aplicado:* resumen reescrito en tres párrafos que describen el documento realmente presentado —consenso en tiempo fijo, co-simulación multitasa de $1\ \text{ms}$/$500\ \text{ms}$, lazo de control sobre ZeroMQ en lock-step, MQTT reducido a telemetría e inyección exógena, grafo de la microrred para inyectar latencia, pérdida y desconexión, y validación en dos niveles—, en presente y con mención explícita de los resultados y de lo que falta. Palabras clave: se retira `MQTT` y se incorporan `Control por Consenso en Tiempo Fijo`, `Co-Simulación Ciberfísica Multitasa` y `ZeroMQ`.

*Verificado en el PDF:* `este anteproyecto`, `enlaces MQTT` y `se simularán` dan **0** ocurrencias; `ZeroMQ en modo lock-step` y `Control por Consenso en Tiempo Fijo` aparecen. 79 páginas · 752 719 B · `0bea7fc5…`.

El cuerpo del documento dice lo contrario, y lo dice explícitamente:

- `IMPLEMENTACION.tex` — el lazo agente ↔ PC Central es ZeroMQ en lock-step; Mosquitto MQTT aparece sólo en la capa de telemetría e inyección exógena (`:176`).
- `JUSTIFICACION.tex` — «Aunque la telemetría global y la inyección exógena utilizan un bróker MQTT …, la toma de decisiones, el algoritmo de consenso y el control de …» se ejecutan sobre ZeroMQ.
- `RESULTADOS.tex` — 3 menciones de ZeroMQ, **0 de MQTT**.

Además el resumen estaba escrito en futuro («se simularán», «generará», «permitirá»), se autodenominaba «este anteproyecto» y no reportaba un solo resultado, cuando el documento ya contiene un benchmark certificado, un ensayo HIL y una campaña de resiliencia. Es el primer párrafo que leerá el jurado y contradecía el capítulo 8.

*Aplicado:* resumen reescrito en tres párrafos que describen el documento realmente presentado —consenso en tiempo fijo, co-simulación multitasa de $1\ \text{ms}$/$500\ \text{ms}$, lazo de control sobre ZeroMQ en lock-step, MQTT reducido a telemetría e inyección exógena, grafo de la microrred para inyectar latencia, pérdida y desconexión, y validación en dos niveles—, en presente y con mención explícita de los resultados y de lo que falta. Palabras clave: se retira `MQTT` y se incorporan `Control por Consenso en Tiempo Fijo`, `Co-Simulación Ciberfísica Multitasa` y `ZeroMQ`.

*Verificado en el PDF:* `este anteproyecto`, `enlaces MQTT` y `se simularán` dan **0** ocurrencias; `ZeroMQ en modo lock-step` y `Control por Consenso en Tiempo Fijo` aparecen.

### H8 · [Alto] Falta la sección de conclusiones y trabajo futuro — **CERRADO POR DECLARACIÓN (2026-11-08)**

El documento terminaba en «Síntesis de resultados», con tres consecuencias verificables: los cuatro **resultados esperados** de `DISENO.tex:43-49` no se declaraban alcanzados en ninguna parte; los pendientes del capítulo —réplica en clúster físico, ensayo del escenario excedente, campaña de semillas múltiples— no tenían dónde constar; y el cierre quedaba a cargo del lector.

*Aplicado:* nueva subsección final **«Cierre del capítulo y trabajo pendiente»** en `RESULTADOS.tex`, que declara que el capítulo no se cierra con conclusiones porque **dos de las tres familias de prueba siguen sin ensayo ejecutado** —excedente de generación (escenarios emitidos e instalados, sin corrida) y réplica de fallas sobre el clúster físico—, y que consolidarlas antes de esas dos corridas afirmaría más de lo que la evidencia sostiene. Con esto el documento no necesita una sección 9, la introducción mantiene sus ocho secciones y el pendiente queda declarado donde el lector lo busca: al final del capítulo de resultados.

### H15 · [Medio] «Consenso No Lineal en Tiempo Fijo» — redundante como nombre de la categoría (observación del autor)

El calificativo no es falso —la convergencia en tiempo fijo exige términos correctores no lineales, porque ninguna ley lineal sobre el grafo acota el tiempo de establecimiento con independencia de las condiciones iniciales— pero **no discrimina**: no existe un «consenso en tiempo fijo lineal» frente al cual distinguirse. Además `TEORIA.tex:138` define la taxonomía real (asintótico, FTS, FxTS) y nunca define «consenso no lineal», y el capítulo 8 llama al esquema «consenso en tiempo fijo (FxTS)».

*Aplicado:* la denominación pasa a **«consenso en tiempo fijo (FxTS)»** en los seis lugares donde funcionaba como nombre propio —`INTRODUCCION:12`, `JUSTIFICACION:6`, `OBJETIVOS:4`, `OBJETIVOS:8`, `PROBLEMA:34` y `IMPLEMENTACION:3`—, y la no linealidad se declara **una sola vez, como propiedad**, en la introducción: «cuya ley incorpora términos correctores no lineales que garantizan una cota de establecimiento independiente de las condiciones iniciales».

*Verificado en el PDF:* `consenso no lineal` → **0** ocurrencias; `consenso en tiempo fijo (FxTS)` → 5; `términos correctores no lineales` → 1.

**Pendiente declarado:** la citación `\citep{Gomes2022FMI30, Liu2025Multirate}` sigue al final de una oración cuyo último sintagma es el despliegue en hardware (Raspberry Pi 5 + Docker), que ninguna de las dos respalda. Ambas sostienen la co-simulación multitasa. Reposicionarlas junto a ese sintagma y apoyar el despliegue en `Mehmood2021` quedó sin aplicar por decisión del autor.

### H9 · [Medio-alto] El marco de tres familias se anuncia pero nunca se introduce

`RESULTADOS.tex:18` anuncia el nivel T2 «organizado por las tres familias del marco de evaluación». Pero:

- No hay encabezado de **Familia 1**: el ensayo de déficit aparece como «Fase I…V» y «Perfil de tensión nodal».
- La primera vez que el lector ve el concepto es `:324`, que empieza «La **segunda** familia del marco de evaluación…», remitiendo a un marco que nunca se presentó y a una primera familia que no tiene nombre.

### H10 · [Medio] El mapa del capítulo quedó desactualizado

`RESULTADOS.tex:18` describe las familias 2 y 3 como «declaradas con su escenario y su criterio». La familia 3 ya **reporta resultados verificados** y la 2 está emitida e instalada, pendiente de ensayo. El mapa describe una fase anterior del capítulo.

### H11 · [Medio] La cadena objetivo → actividad → resultado está rota

`DISENO.tex` define 13 actividades numeradas (1.1–4.3), y **ninguna otra sección vuelve a mencionarlas**. En particular, el capítulo de resultados ya no remite a las actividades 3.3 (proxy de contingencias) ni 4.2 (tolerancia a latencia y pérdida), que son las que sostienen el cuarto objetivo. La remisión existía en el párrafo de validez y se perdió al reescribirlo para incorporar la campaña de resiliencia.

### H12 · [Medio] 33 de 55 ecuaciones etiquetadas nunca se referencian

Hay 55 `\label{eq:…}` y sólo 22 aparecen en un `\ref`/`\eqref`. Las 33 restantes son etiquetas muertas: el texto enuncia la ecuación y no vuelve a señalarla. O se referencian donde corresponde (discusión, contraste, trazabilidad al código) o se retiran las etiquetas.

### H13 · [Medio-bajo] Ninguna sección tiene etiqueta

Cero `\label{sec:…}` y cero `\ref{sec:…}`: todas las remisiones entre capítulos son verbales («el capítulo de implementación», «el marco teórico»). Funciona hoy, pero es frágil ante cualquier reordenamiento y no es verificable por un script.

### H14 · [Bajo] Código muerto en el planteamiento del problema

`PROBLEMA.tex:10` conserva comentada la subsección `% El Conflicto Metodológico: La Pérdida del Anclaje Físico`. El contenido no se perdió —está desarrollado en prosa en las líneas siguientes—, pero la fuente arrastra una línea desactivada.

---

## 3. Orden de intervención propuesto

| Orden | Hallazgo | Coste | Efecto |
|---|---|---|---|
| 1 | H7 · resumen y palabras clave | reescritura de 10 líneas | ✅ hecho — contradicción eliminada del PDF |
| 2 | H8 · conclusiones y trabajo futuro | subsección de cierre | ✅ hecho — pendiente declarado, sin sección 9 |
| 3 | H9 + H10 · marco de familias y mapa del capítulo | 2 encabezados y 1 párrafo | simetría del capítulo y mapa fiel |
| 4 | H11 · trazabilidad actividad → resultado | 1 párrafo | sostiene el cuarto objetivo |
| 5 | H12 + H13 + H14 | mecánico | higiene de fuentes |

Ninguno de los ocho hallazgos exige tocar el preámbulo ni las cifras del capítulo 8.
