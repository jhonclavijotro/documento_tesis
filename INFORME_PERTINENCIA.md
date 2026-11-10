# Informe de pertinencia de citaciones — lote 1 (Introducción y Planteamiento del problema)

**Método.** Para cada sitio de cita se responde primero, en una línea y sin jerga, *qué demuestra la fuente* —a partir de su resumen en CrossRef o, cuando no lo hay, de su registro bibliográfico— y después se contrasta con lo que la frase le atribuye. Si la fuente no puede sostener la frase, se marca.

**Veredictos:** `PERTINENTE` · `PARCIAL` (sostiene parte de la frase) · `DUDOSA` (no se puede confirmar sin leer el artículo) · `NO PERTINENTE` (la fuente no trata lo que la frase afirma).

---

## Introducción

| Cita | Qué demuestra la fuente | Veredicto |
|---|---|---|
| `IRENA2026` | A finales de 2025 las renovables fueron el **49 %** de la capacidad instalada mundial y el **85,6 %** de las adiciones anuales (verificado en el PDF del informe) | **PERTINENTE** |
| `Mehrzad2025` | Revisión de la inercia en sistemas eléctricos con renovables | **PERTINENTE** |
| `Mamun2026`, `Altin2023MultiAgent` | Revisiones de sistemas multiagente para control descentralizado de microrredes | **PERTINENTE** |
| `Jasim2023` | MICrorredes aisladas sufren desviaciones de frecuencia/tensión y propone consenso MAS para restaurarlas | **PERTINENTE** |
| `Diaz2025` | Marcos IoT para controladores genéricos distribuidos de microrred, en modo conectado e isla | **PERTINENTE** |
| `Gomes2022FMI30`, `Liu2025Multirate` | Estándar FMI 3.0 y marco de co-simulación multitasa con paso variable | **PERTINENTE** (ya reposicionadas) |
| `Mehmood2021` | Computación en el borde para redes inteligentes | **PERTINENTE** |
| `Pompodakis2022Sensitivity` | Flujo de potencia trifásico sensitivo con controladores locales de tensión en distribución | **PARCIAL**: sostiene el acoplamiento tensión-potencia, no el término $P$-$Q$ frente a $V$-$\theta$ |
| `Sowa2023` | Consenso distribuido con medidores de alta tasa en redes con inversores | **PARCIAL**: no es una fuente sobre acoplamiento $P$-$Q$ / $V$-$\theta$ |
| `Verma2024` | *Restoration of extra-high voltage power grids* (EPSR) | **DUDOSA**: el título remite a restauración de redes de muy alta tensión, no a microrredes con FNCER en modo isla |
| `TaverasCruz2025` | Protección adaptativa basada en sistemas multiagente | **DUDOSA**: se le atribuyen límites del control centralizado (punto único de falla, escalabilidad, cuellos de botella) que una fuente de protección no establece |
| `AlvarezLopez2026` | Revisión de IA para gestión energética distribuida en arquitecturas IoT-Edge-Cloud | **PARCIAL**: sostiene la autonomía en el borde, no la coordinación exclusiva con vecinos |
| `Muszynski2026EnergyTwin` | Sistema multiagente para simular y coordinar microrredes | **DUDOSA**: se le usa para establecer la brecha entre simuladores de potencia y marcos MAS; es un caso de la segunda categoría, no el diagnóstico de la brecha |
| `Khanna2025`, `Haid2022CosimCorrector`, `Kyllingstad2025CosimErrors` | Marco multi-capa con pronóstico y blockchain; correctores de co-simulación; errores por cambio de paso | **NO PERTINENTE** para la frase sobre MQTT: ninguna de las tres trata MQTT (H16) |

## Planteamiento del problema

| Cita | Qué demuestra la fuente | Veredicto |
|---|---|---|
| `Mehrzad2025` | Inercia y RoCoF con generación basada en convertidores | **PERTINENTE** |
| `Jasim2023` | Desviaciones de frecuencia/tensión en microrredes aisladas y restauración por consenso | **PERTINENTE** |
| `Mamun2026`, `Altin2023MultiAgent` | Control secundario distribuido con MAS y consenso sobre grafos | **PERTINENTE** |
| `Shrivastava2023FiniteTime` | Controlador secundario distribuido en tiempo finito para microrredes AC con modelo ciberfísico | **PERTINENTE** para la no linealidad en lazo cerrado |
| `Barzegari2022Resilient` | Detección de inyección de datos falsos con observadores de modos deslizantes en microrred DC | **PARCIAL**: sostiene resiliencia frente a ataques, no frente a contingencias estocásticas de comunicación |
| `Pompodakis2022Sensitivity`, `Sowa2023` | Flujo sensitivo trifásico; consenso con medidores de alta tasa | **PARCIAL**: sostienen la caída de tensión en alimentadores, no la afirmación completa |
| `Olayanju2025ConsensusFreq` | Control secundario de frecuencia por consenso ante impedimentos de la red | **PARCIAL**: sostiene retardos y pérdidas como impedimentos, no el comportamiento de MQTT |
| `AlvarezLopez2026` | Revisión de IA en IoT-Edge-Cloud con restricciones de latencia | **PARCIAL**: no es una fuente sobre pérdida de paquetes en MQTT |
| `Liu2025Multirate`, `Haid2022CosimCorrector` | Co-simulación multitasa de convertidores; correctores de co-simulación | **PARCIAL**: sostienen las escalas µs-ms, no la respuesta electroquímica del BESS (s-min) que la frase incluye |
| `Kyllingstad2025CosimErrors` | Errores de co-simulación por cambio de tamaño de paso | **PERTINENTE** para la divergencia numérica del acoplamiento |
| `Gomes2022FMI30` | Estándar FMI 3.0 para co-simulación acoplada | **PERTINENTE** |
| `Verma2024` | Restauración de redes de muy alta tensión | **DUDOSA / probablemente NO PERTINENTE**: se le atribuye la interfaz exclusiva por convertidores de PV, eólica y BESS |

## Reparación de las cuatro citas señaladas (2026-11-08)

Se revisó qué demuestra cada fuente —título y resumen en OpenAlex/CrossRef— y se reparó por reposición, no por sustitución a ciegas: la cita se mueve al sintagma que sí respalda, o se cambia por una entrada del propio `.bib` que lo respalda.

### `Verma2024` — retirada

*Restoration of extra-high voltage power grids through synchronous and asynchronous hydro units during blackout* (EPSR, 2023). Es un artículo de restauración de redes de muy alta tensión con unidades hidroeléctricas; no trata microrredes con FNCER, ni la interfaz por convertidores, ni la dinámica EMT, ni el RoCoF. Estaba citada en **cuatro** lugares y ninguno era pertinente:

| Sección | Frase | Ahora |
|---|---|---|
| Introducción | microrredes con FNCER en modo conectado o isla | `Mamun2026, Altin2023MultiAgent` |
| Problema | PV, eólica y BESS se interfazan solo por convertidores | `Mehrzad2025` |
| Antecedentes | transitorios EMT y lazos `dq` | `Mehrzad2025, Liu2025Multirate` |
| Marco teórico | RoCoF crítico ante $H \to 0$ | `Mehrzad2025` |

La entrada se retiró del `.bib`: el documento pasa de 52 a **51 referencias**, todas citadas.

### `TaverasCruz2025` — conservada solo donde sostiene

*Adaptive protection based on MAS for AC microgrids: A review* (Applied Energy, 2024). Su resumen ofrece autonomía, tolerancia a fallos y robustez frente a fallas y topologías cambiantes. No establece los límites del control centralizado ni la redundancia de SCADA ni las métricas de desempeño.

| Sección | Frase | Ahora |
|---|---|---|
| Introducción | punto único de falla, escalabilidad, cuellos de botella | `Khayat2020, Altin2023MultiAgent` — la revisión de arquitecturas de control secundario es exactamente la fuente de esa comparación |
| Justificación | SCADA con fibra óptica redundante | `Khayat2020` |
| Diseño | lista de métricas | `Barzegari2022Resilient` |
| Problema | evaluación de resiliencia | `Barzegari2022Resilient` |
| Antecedentes | aislar enlaces antes del colapso del consenso | **se conserva**: es lo que la revisión de protección adaptativa sostiene |

### `Muszynski2026EnergyTwin` — conservada y matizada

*EnergyTwin: A Multi-agent System for Simulating and Coordinating Energy Microgrids* (LNCS, 2026). Es un caso de marco multiagente para coordinar microrredes; no es el diagnóstico de la brecha entre simuladores y marcos MAS, y no hay resumen público que permita atribuirle una simplificación concreta del circuito.

- **Antecedentes**: se conserva sin cambios — allí ilustra que un simulador de transitorios interactúa con un entorno de agentes, que es su contenido.
- **Introducción y Problema**: la frase pasa de afirmar a describir una tendencia (`tienden a resolver el circuito con balances algebraicos`, `aproximaciones lineales`) y se acompaña de `Khanna2025`, que es otro marco multiagente sin modelo eléctrico.
- **Justificación**: se retira y queda `Altin2023MultiAgent`, que sí es la revisión del estado del arte de MAS en microrredes.

### Verificación

`latexmk -C` + `latexmk -pdf`: **79 páginas · 756 084 B · `b93fcc12…`**, 0 errores, 0 citas indefinidas, 0 avisos de BibTeX, sin `??`. Auditoría de referencias: 51 citadas / 51 entradas, ninguna huérfana en ningún sentido. En el PDF, `Verma` da **0** apariciones.

## Conclusión del lote 1

- **1 no pertinente confirmada** (H16, frase de MQTT), con las tres fuentes ajenas al tema.
- **1 no pertinente en cuatro secciones** (`Verma2024`) — **reparada y retirada del `.bib`**.
- **3 atribuciones dudosas** (`TaverasCruz2025`, `Muszynski2026EnergyTwin` ×2) — **reparadas**.
- **8 citas parciales**: sostienen una parte de la frase pero no el conjunto. No son errores graves —la frase queda apoyada a medias—, pero conviene repartir la cita al sintagma que sí respaldan, como se hizo con Gomes y Liu.

**Pendiente:** lotes 2 a 4 — Antecedentes (63 instancias), Marco teórico (33), Diseño e Implementación (32).
