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

### H9 · [Medio-alto] El marco de tres familias se anuncia pero nunca se introduce — **CORREGIDO (2026-11-08)**

El mapa del capítulo prometía tres familias y sólo dos tenían encabezado: el ensayo de déficit aparecía como «Fase I…V» y el lector topaba con «la segunda familia» sin haber leído de la primera.

*Aplicado:* nuevo encabezado **«Familia 1: déficit de capacidad»** antes de la Fase I, con un párrafo de apertura que define la familia, y «Plataforma y contrato de muestreo» queda como preámbulo común a las tres. Las tres familias son ahora paralelas en jerarquía.

### H10 · [Medio] El mapa del capítulo quedó desactualizado — **CORREGIDO (2026-11-08)**

El mapa describía las familias 2 y 3 como «declaradas con su escenario y su criterio», y el apartado de T2 decía que sus corridas «aún no están publicadas».

*Aplicado:* el mapa distingue ahora los tres estatutos —déficit analizada, excedente «declarada con su escenario y su criterio a la espera de corrida», fallas «reportada con su ensayo de resiliencia»— y el apartado de T2 hace la misma distinción. Se retira además «en un único escenario» de la limitación del banco, que ya no describe su alcance.

### H11 · [Medio] La cadena objetivo → actividad → resultado está rota — **CORREGIDO (2026-11-08)**

`DISENO.tex` define 13 actividades y ninguna otra sección las mencionaba.

*Aplicado:* nuevo párrafo en «Alcance y organización de la validación» que ata cada bloque del capítulo a sus actividades: el benchmark a 1.1, 1.2, 1.3, 4.1 y 4.3; el banco HIL a 3.1 y 3.2; la familia de fallas a 3.3 y 4.2; y la familia de excedente a 4.1 en el régimen excedentario.

### H12 · [Medio] Ecuaciones que exhibían número sin ser invocadas — **CORREGIDO (2026-11-08)**

*Criterio:* el número se reserva para lo que el lector puede necesitar consultar. Se conserva en (i) toda ecuación invocada desde el texto y (ii) las leyes de modelo y los límites normativos que el evaluador puede querer verificar, aunque nadie los cite. El resto pasa a visualización sin número.

*Primer paso:* se retiraron 32 etiquetas `eq:` muertas y se conservó y citó la de la ecuación de oscilación de resultados.

*Segundo paso:* **18 entornos** (22 líneas numeradas) pasaron a visualización sin número —7 en `TEORIA`, 6 en `IMPLEMENTACION`, 5 en `RESULTADOS`—: la discretización del PLL, las cotas de SoC, la definición de la Laplaciana, la del operador `sig`, la cota de la derivada de Lyapunov, la actualización discreta del lazo secundario y la definición de `f_nadir`; el cálculo del `sleep`, la firma de `step()`, la síntesis de tensiones `abc`, la actualización discreta de `V_dc`, las recursiones de `ΔV`, `ΔQ` y `Δω`, y las cinco sustituciones aritméticas del capítulo de resultados.

*Se conserva el número, aunque no se citen,* en las ecuaciones de modelo que el jurado puede querer consultar: dinámica `dq` del convertidor, función de transferencia del SRF-PLL, bus DC fotovoltaico, estado de carga del BESS, potencia y par eólicos, límite de aparente del inversor, matrices de sensibilidad, paso de Euler del micro-paso, evaluación lineal de sensibilidades y matriz de Gilbert-Elliott.

*Verificado:* la numeración del documento baja de **57 a 35** ecuaciones numeradas, de las cuales **23 están referenciadas y 12 se numeran por decisión editorial**. Quedan **0** etiquetas sin referenciar. El PDF pasa de 754 626 a **754 038 B** con las mismas 79 páginas, 0 errores, 0 referencias indefinidas y sin `??`; la ecuación de oscilación se lee ahora como (35).

### H13 · [Medio-bajo] Ninguna sección tenía etiqueta — **CORREGIDO (2026-11-08)**

*Diagnóstico:* 37 etiquetas y 70 referencias cruzadas sobre flotantes y ecuaciones, y **cero** sobre secciones: las remisiones entre capítulos eran cinco frases en prosa. Con `hyperref` y `colorlinks`, las 70 numéricas se imprimen como enlaces y las verbales no llevan a ninguna parte; peor aún, una remisión verbal obsoleta sigue siendo gramaticalmente correcta, de modo que ningún script puede detectarla.

*Aplicado:*
1. **Ocho etiquetas de sección** (`sec:problema` … `sec:resultados`), una por sección numerada.
2. **Tres remisiones convertidas** a `
ef`: `ANTECEDENTES` remite a `sec:implementacion`, y `IMPLEMENTACION` a `sec:teoria` y a `sec:resultados` (dos veces).
3. **Trece actividades etiquetadas** en `DISENO` mediante una macro local `ct{3.3}`, que imprime el identificador y deja la etiqueta `act:3.3` con ese mismo texto: así la referencia no depende de la numeración de la lista y sobrevive a cualquier renumeración.
4. Las **nueve citas de actividad** del capítulo de resultados pasan a `
ef{act:…}`.

*Verificado en el PDF:* `sección 5`, `sección 7` y `capítulo 8` se imprimen resueltos; las actividades se leen como 1.1, 1.2, 1.3, 3.1, 3.2, 3.3, 4.1, 4.2 y 4.3; los trece rótulos «Actividad X.Y:» siguen intactos; sin `??` y sin avisos de etiquetas duplicadas. 79 páginas · 754 215 B.

*Incidencia durante la edición:* el ejecutor de comandos colapsó las barras invertidas de tres `
ef` y las convirtió en retornos de carro; se detectó con un volcado `repr` y se repararon antes de compilar. Regla adoptada: los cambios con barras invertidas se escriben en un archivo `.py` y no por entrada estándar.

### H14 · [Bajo] Tres encabezados comentados despojaban al capítulo 1 de su estructura — **CORREGIDO (2026-11-08)**

No era una línea muerta: eran **tres `\subsection` comentados** que organizaban todo el planteamiento del problema, mientras el texto seguía desarrollando exactamente esos tres bloques en ese orden. Consecuencias verificadas:

- El capítulo 1 aparecía en el índice con **un solo apartado** («Pregunta de Investigación») tras tres páginas de prosa continua (pp. 11–13), frente a 2–6 apartados en las demás secciones.
- La introducción (`INTRODUCCION.tex:16`) anunciaba los tres movimientos del capítulo —crisis de inercia, conflicto metodológico, pregunta—, de modo que el índice contradecía la descripción del propio autor.
- El concepto que define la tesis, la pérdida del anclaje físico, circulaba en el cuerpo sin apartado donde buscarlo.

*Aplicado:* reactivados los tres encabezados y armonizado el término inglés con el que usa el cuerpo: `(\textit{No Physical Grounding})`, igual que el ítem b) de la enumeración, en lugar de `(\textit{Physical Grounding})`, que invertía el sentido del argumento.

*Verificado en el PDF:* el índice del capítulo 1 muestra **1.1 Contexto de la Transición Energética y Vulnerabilidad Física**, **1.2 El Conflicto Metodológico: La Pérdida del Anclaje Físico (No Physical Grounding)**, **1.3 No Linealidad Inducida, Heterogeneidad Temporal y Degradación Ciber-Física** y **1.4 Pregunta de Investigación**; ninguna línea comentada queda en la fuente. 79 páginas · 756 311 B · sin `??`.


---

## 3. Orden de intervención propuesto

| Orden | Hallazgo | Coste | Efecto |
|---|---|---|---|
| 1 | H7 · resumen y palabras clave | reescritura de 10 líneas | ✅ hecho — contradicción eliminada del PDF |
| 2 | H8 · conclusiones y trabajo futuro | subsección de cierre | ✅ hecho — pendiente declarado, sin sección 9 |
| 3 | H9 + H10 · marco de familias y mapa del capítulo | 2 encabezados y 1 párrafo | ✅ hecho |
| 4 | H11 · trazabilidad actividad → resultado | 1 párrafo | ✅ hecho — las 13 actividades vuelven a estar enlazadas |
| 5 | H12 + H13 + H14 | mecánico | los tres cerrados |

Ninguno de los ocho hallazgos exige tocar el preámbulo ni las cifras del capítulo 8.
