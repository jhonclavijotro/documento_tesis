# FIGURAS.md — Guía para generar las tres figuras conceptuales con IA externa

**Documento destino:** `D:\TEXTOS\TESIS` — sección 7 (Arquitectura e Implementación) y sección 8 (Resultados y Discusión).
**Fecha:** 2026-11-08
**Estado:** las tres figuras **no** se integran todavía al manuscrito. Se generarán con una herramienta de imagen externa y sólo si el resultado no es apto se recurre a la versión vectorial ya disponible.
**Versión de respaldo (ya generada, vectorial):** `Figuras/fig_estructura.pdf`, `Figuras/fig_flujo_datos.pdf`, `Figuras/fig_validacion.pdf`, reproducibles con `figuras_conceptuales.py` (matplotlib, Type 42, 14,81 cm de ancho).

---

## 1. Regla que decide si una imagen entra al documento

La figura se acepta sólo si cumple **las cinco condiciones**. Si falla una, se descarta y se usa la versión vectorial de respaldo.

1. **Texto legible y correcto.** Todos los rótulos escritos sin errores, en español, con las cadenas exactas que fija este documento. Si la IA deforma letras, se usa la variante «sin texto» (§4) y los rótulos se añaden después.
2. **Vectorial al final.** El manuscrito exige PDF vectorial con fuentes incrustadas. Una imagen de mapa de bits debe vectorizarse o redibujarse antes de insertarse; si eso degrada el texto, se descarta.
3. **Trazabilidad.** Nada de elementos decorativos inventados: sólo los bloques y relaciones que figuran aquí, que provienen del código y de los artefactos reales del proyecto.
4. **Coherencia con el manuscrito.** Tipografía sans de 8–9 pt al ancho final, sin título dentro del gráfico (el título va en el pie), una sola leyenda que no tape elementos, fondo blanco, sin sombras ni 3D.
5. **Ancho de inserción** `0.95\textwidth` = **14,81 cm** (nunca 1,0). Relación de aspecto: A ≈ 14,81 × 9,6 cm; B ≈ 14,81 × 9,0 cm; C ≈ 14,81 × 8,8 cm.

**Paleta.** Gris azulado `#E9F0F7` para el borde, gris neutro `#F7F7F7` para infraestructura, crema `#FBF6EA` para datos, verde `#E8F2E8` (validado), ámbar `#FDF3DD` (pendiente), rojo `#FBE7E5` (en construcción). Trazos `#333333`, 0,8 pt. Máximo cinco colores de relleno por figura.

---

## 2. Lo que cambió en el código y en los escenarios (obligatorio reflejarlo)

Estas modificaciones son recientes y **no** aparecen en las figuras antiguas del capítulo. Cualquier generación que las omita queda desactualizada.

| Cambio | Qué implica en las figuras |
|---|---|
| **Renombrado del controlador** (S-35) | El módulo es `Agents/fixed_time_consensus.py` (tiempo **fijo**, FxTS). `Agents/finite_time_consensus.py` sólo existe como *shim* de compatibilidad. No rotular el control como «finite time». |
| **Régimen excedentario** (S-36) | Existen absorción en el BESS (consigna negativa, acotada por SoC) y **recorte de la fuente solar** (`curtail_ratio` sobre el MPP), con índice de reparto propio. El bloque de recursos debe admitir flujo bidireccional en el BESS y techo de inyección en el PV. |
| **Proxy de fallas de red** | `Agents/network_impairment_proxy.py` inyecta latencia, pérdida de paquetes y desconexión de enlace sobre ZeroMQ. Debe aparecer como elemento del enlace, **no** como un bloque del PC Central. |
| **Escenarios nuevos de OpenCode** | `ESC-HIL-005` (rampas solares + escalones de demanda) está generado y validado en el espacio de trabajo de OpenCode (`D:\Opencode\TESIS_DATA\escenarios\`), **no instalado** en el proyecto. `ESC-HIL-006` (excedente con ventana declarada) y `ESC-HIL-007` (referencia sin excedente) están **instalados** en `Forms/escenarios_generados/` y **no activados**. Ninguno de los tres se ha ejecutado. |
| **Séptimo artefacto de configuración** (D-25) | Desde D-25 cada escenario nuevo emite, además de `datos_meteorologicos.csv`, `datos_demanda.csv`, `topologia_red_8nodos.csv` y `plantilla_configuracion_cosimulacion.json`, un archivo propio `contingencias_telematicas.csv`. Lo incluyen `ESC-HIL-006` y `ESC-HIL-007`; `ESC-HIL-001`, `003` y `005` son anteriores al contrato y **no** lo tienen. `ACTIVO.txt` sigue apuntando a `ESC-HIL-003_consolidado_rev5`. |
| **Corrida canónica vigente** | `20261108T161211_bench-v2_seed42` (manifiesto `115a6eb9…`), con delta numérico cero frente a sus tres predecesoras. Si una figura cita un identificador de corrida, es este. |
| **MQTT no es el lazo de control** | El lazo agente↔PC Central es **ZeroMQ en lock-step a 2 Hz**. MQTT (`GUI/mqtt_publisher.py`) sólo publica telemetría hacia el tablero. Dibujarlos en el mismo plano es un error factual. |

---

## 3. Figura A — Estructura del proyecto

**Objetivo.** Que el lector vea en un golpe de vista qué piezas componen el sistema, dónde viven y qué papel cumple cada una.
**Ubicación prevista.** Sección 7, junto a la descripción de la arquitectura.
**Rotulación (usar estos textos, sin sinónimos):** «Figura X. Estructura del proyecto: módulos de borde, orquestador central, recursos modelados y cadena de datos.»

**Elementos y rótulos exactos**

- Bloque 1, título **«Borde: agentes en Raspberry Pi 5 (×6)»**: `Agents/distributed_node_runner.py` · `Agents/fixed_time_consensus.py` · `Agents/node_dynamic_process.py` · `Agents/network_impairment_proxy.py` · `Agents/monitor_node_service.py`
- Bloque 2, título **«PC Central: orquestador 10.0.0.156»**: `Central_PC/master_clock_zmq.py` · `Central_PC/power_flow_clock_server.py` · `Central_PC/power_flow_fbs.py` · `Central_PC/sensitivity_matrices.py` · `Central_PC/communication_emulator.py`
- Bloque 3, título **«Recursos modelados (planta)»**: `Diesel/` · `Solar/` · `BESS/` · `Demanda/multi_load_process.py`
- Bloque 4, título **«Interfaz y monitoreo»**: `GUI/gui_command_center.py` · `GUI/mqtt_publisher.py` · tablero HTTP
- Banda inferior, título **«Datos, escenarios y evaluación»**:
  - `Forms/escenarios_generados/ESC-HIL-00x/` → `datos_meteorologicos` · `datos_demanda` · `topologia` · `contingencias_telematicas`
  - `outputs/benchmark/` → `harness` · `metrics_v2` · `results/<run_id>` · `CURRENT.json`
  - `output_data/telemetry_monitor_cluster_8nodes_hil.csv`

**Relaciones.** Flecha doble entre Bloque 1 y Bloque 2 rotulada «ZeroMQ · lock-step» (bajada: «$V$ pu, $f$»). Flecha Bloque 1 → Bloque 3 rotulada «consigna» y retorno. Flecha Bloque 4 → banda de datos rotulada «telemetría». Ambas columnas vierten en la banda inferior.

**Prompt (inglés, para el generador)**
> Clean technical block diagram, flat vector style, white background, no shadows, no 3D, thin dark gray outlines. Four rounded rectangles in a 2×2 upper area plus one wide band at the bottom. Top-left block: edge computing with six small single-board computers. Top-right block: a central orchestrator PC. Middle-left block: three generation resources (diesel generator, solar PV array, battery storage) and a load model. Middle-right block: a monitoring dashboard. Bottom band: data files, benchmark outputs and a telemetry CSV. Double-headed arrow between the two top blocks labeled "ZeroMQ lock-step"; arrow from edge block to resources labeled "consigna"; arrow from dashboard to bottom band labeled "telemetría". Palette: pale blue-gray for edge and central, neutral gray for infrastructure, pale cream for data. Labels in Spanish, sans-serif, 8 pt equivalent, straight horizontal text only.

**Negative prompt**
> photo, realistic, 3D, isometric, gradients, drop shadows, glow, icons of houses or clouds, decorative, circuit-board texture, garbled text, misspelled words, vertical or rotated text, watermark, logo, colorful neon.

---

## 4. Figura B — Flujo de datos

**Objetivo.** Mostrar el ciclo cerrado de la co-simulación: quién manda, quién responde, con qué cadencia y dónde puede fallar.
**Ubicación prevista.** Sección 7, junto al motor de co-simulación multitasa.
**Pie previsto.** «Figura Y. Flujo de datos del lazo cerrado: consigna y retorno entre el nodo de borde y el PC Central, cadencia de los dos pasos temporales y plano de monitoreo.»

**Elementos y rótulos exactos**

- Bloque A, título **«Nodo DER i (borde)»**: «runner del agente» · «ley FxTS» · «micro-paso $h$ = 1 ms» · «retenedor ZOH»
- Bloque B, título **«Enlace de comunicación»**: «ZeroMQ REQ/REP» · «latencia · pérdida» · «desconexión de enlace» · «último estado conocido»
- Bloque C, título **«PC Central»**: «servidor maestro» · «lock-step $H$ = 0,5 s» · «flujo de potencia (FBS)» · «matrices de sensibilidad»
- Rótulo superior sobre las flechas de ida: **«consigna $P_{\text{ref}},\ Q_{\text{ref}}$ →»**
- Rótulo inferior sobre las flechas de retorno: **«← $P_i,\ Q_i$ inyectadas y $V_{\text{pcc}}$ de retorno»**
- Banda 1, título **«Plano de monitoreo — no participa del lazo de control»**: «MQTT desde la interfaz (`GUI/mqtt_publisher.py`): telemetría, registro y tablero»
- Banda 2, título **«Tiempos del lazo»**: «micro-paso $h$ = 1 ms dentro del nodo · macro-paso $H$ = 0,5 s en el PC Central (2 Hz)» · «retenedor de orden cero entre macro-pasos · consenso evaluado una vez por macro-paso»

**Prompt (inglés)**
> Clean horizontal technical flow diagram, flat vector, white background. Three rounded rectangles in one row: left "edge node", centre narrow "communication link", right "central PC". Two arrows from left to right and two arrows from right to left crossing the centre block, labelled above and below. Below the row, one wide band for a monitoring plane marked as not part of the control loop, and a second wide band listing timing information. Thin dark outlines, pale blue-gray boxes, neutral gray for the link, pale cream for the monitoring band. Spanish labels, sans-serif, horizontal, 8 pt equivalent.

**Negative prompt**
> cloud icons, wifi symbols, antenna drawings, servers in racks, human figures, arrows with gradients, dashed glow, text at angles, invented English acronyms, watermark.

> **Advertencia específica.** Si el generador dibuja MQTT dentro del bloque de enlace o como canal entre agentes, la figura es **incorrecta** y se descarta: MQTT está únicamente en el plano de monitoreo.

---

## 5. Figura C — Implementación en los ejercicios de validación

**Objetivo.** Que el lector vea los dos niveles de validación y, colgando del nivel físico, las tres familias de escenario con su estado real.
**Ubicación prevista.** Sección 8, en «Alcance y organización de la validación».
**Pie previsto.** «Figura Z. Organización de la validación: benchmark numérico (T1) y banco físico HIL (T2), con las tres familias de escenario y su estado de evidencia.»

**Elementos y rótulos exactos**

- Bloque superior izquierdo, título **«Nivel T1: benchmark numérico»**: «9 variantes de control · semilla 42» · «8 gates (G1–G8) · corrida canónica» · «planta algebraico-cinemática (D-13)»
- Bloque superior derecho, título **«Nivel T2: banco físico HIL»**: «6 Raspberry Pi 5 + PC Central» · «300 s a 2 Hz · 8 barras de 400 V» · «tres familias de evaluación (D-24)»
- Bloque inferior izquierdo, título **«Familia 1: déficit»**: «ESC-HIL-001 / 003» · «12,59 kW > 11,54 kW» · «validada»
- Bloque inferior central, título **«Familia 2: excedente»**: «ESC-HIL-006 y 007» · «holgura +2,9 a +3,5 kW» · «ensayo pendiente»
- Bloque inferior derecho, título **«Familia 3: fallas»**: «latencia · pérdida · corte» · «50–500 ms · 0–30 %» · «en construcción»
- Relación: del bloque T2 baja una línea que se reparte en los tres bloques inferiores. T1 **no** se conecta con las familias.

**Prompt (inglés)**
> Clean two-level validation diagram, flat vector, white background. Two rounded rectangles on top row (numerical benchmark and hardware-in-the-loop test bench) and three smaller rounded rectangles on the bottom row (three scenario families), connected only from the right top block to the three bottom blocks through a single branching line. Colour code the bottom row: light green (validated), light amber (pending), light red (under construction). Spanish labels, sans-serif, 8 pt equivalent, horizontal only.

**Negative prompt**
> flowcharts with diamonds, decision triangles, gears, stopwatch icons, traffic lights, percentages in red circles, gradients, 3D, watermark, invented scenario names.

> **Advertencia específica.** La familia 2 **no** está validada: la capacidad existe en el código y el escenario está emitido, pero no hay corrida. Si la imagen la muestra como aprobada, induce a error en la defensa.

---

## 6. Flujo de trabajo con la IA externa

1. **Primera pasada con texto.** Usar el prompt de la figura con los rótulos incluidos. Revisar letra por letra: nombres de archivo, acrónimos y cifras.
2. **Si el texto sale deformado** (lo habitual), usar la variante **sin texto**: quitar del prompt la última frase sobre rótulos y sustituirla por *«no text, no letters, empty boxes»*. Después se añaden los rótulos en Inkscape o en LaTeX sobre la imagen limpia. Es el camino recomendado para nombres de archivo con guiones y guiones bajos, que ningún generador reproduce bien.
3. **Composición.** Exportar a la mayor resolución posible (≥ 3 000 px de ancho) y comprobar que la relación de aspecto coincide con la del cuadro 1.
4. **Vectorización.** Trazar en Inkscape («Trayecto > Vectorizar mapa de bits», modo color, dos o tres colores) o redibujar los bloques. Verificar que el PDF final no tenga fuentes sustituidas ni texto convertido en curvas ilegibles.
5. **Inserción.** Guardar como `Figuras/fig_estructura.pdf`, `Figuras/fig_flujo_datos.pdf` y `Figuras/fig_validacion.pdf` (sobrescribiendo el respaldo) e insertar en el `.tex` con:
   `\includegraphics[width=0.95\textwidth]{Figuras/fig_estructura.pdf}` dentro de un entorno `figure[H]`, con `\caption` y `\label`.
6. **Verificación final.** Compilar y revisar en el PDF: que el texto de la figura se lea al tamaño impreso, que ninguna etiqueta toque el marco y que el pie no repita cifras que ya están dentro del gráfico.

---

## 7. Errores que invalidan una figura

- Rotular el controlador como «finite time» en lugar de **tiempo fijo (FxTS)**.
- Presentar el régimen excedentario como validado.
- Mostrar el banco de 21 nodos como si existiera: está declarado trabajo futuro.
- Dibujar MQTT en el lazo de control.
- Omitir `contingencias_telematicas.csv` entre los artefactos de escenario.
- Citar una corrida canónica distinta de `20261108T161211_bench-v2_seed42`.
- Usar iconografía realista (casas, nubes, servidores 3D) en un diagrama de arquitectura.
- Texto en inglés, siglas inventadas o cifras que no provengan de los artefactos.

---

## 8. Respaldo vectorial disponible

Si la IA no entrega una figura apta, se usan las ya generadas:

| Figura | Archivo | Tamaño | Regeneración |
|---|---|---|---|
| A · Estructura | `Figuras/fig_estructura.pdf` | 14,81 × 9,60 cm | `python figuras_conceptuales.py` |
| B · Flujo de datos | `Figuras/fig_flujo_datos.pdf` | 14,81 × 9,00 cm | idem |
| C · Validación | `Figuras/fig_validacion.pdf` | 14,81 × 8,80 cm | idem |

Ambas rutas —IA externa y script— producen el mismo contenido semántico; lo que cambia es el acabado. La decisión se toma figura por figura, y la que entre al manuscrito debe cumplir las cinco condiciones del §1.
