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

## Conclusión del lote 1

- **1 no pertinente confirmada** (H16, frase de MQTT), con las tres fuentes ajenas al tema.
- **1 probable no pertinente repetida en dos secciones** (`Verma2024`: el título no corresponde a la afirmación).
- **3 atribuciones dudosas** que exigen leer el artículo antes de mantenerlas (`TaverasCruz2025`, `Muszynski2026EnergyTwin` ×2).
- **8 citas parciales**: sostienen una parte de la frase pero no el conjunto. No son errores graves —la frase queda apoyada a medias—, pero conviene repartir la cita al sintagma que sí respaldan, como se hizo con Gomes y Liu.

**Pendiente:** lotes 2 a 4 — Antecedentes (63 instancias), Marco teórico (33), Diseño e Implementación (32).
