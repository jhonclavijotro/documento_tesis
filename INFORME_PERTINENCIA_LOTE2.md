# Informe de pertinencia — lote 2: Antecedentes y estado del arte

**Método.** Igual que el lote 1: primero qué demuestra la fuente (resumen en CrossRef/OpenAlex o, si no lo hay, su registro), después qué le atribuye la frase. 40 instancias de cita, 45 claves distintas.

**Resultado global:** 31 pertinentes · 4 parciales · 4 dudosas · 1 fila de tabla con dos claves que no corresponden.

---

## Lo que no corresponde

### N1 · La fila «tiempo fijo» de la tabla de arquitecturas cita dos trabajos que no son de tiempo fijo

`ANTECEDENTES.tex:32` — la última fila, que describe el esquema de este trabajo, cita `\citep{Polyakov2012, Zhang2024, Zhao2025}`.

- `Polyakov2012` es el artículo fundacional del tiempo fijo: **correcto**.
- `Zhang2024` — *Distributed Secondary Control for Island Microgrids With Expected Dynamic Performance Under Communication Delays*: control secundario con retardos, sin cota de establecimiento independiente del estado inicial.
- `Zhao2025` — *Data-Driven Fully Distributed Fault-Tolerant Consensus…*: consenso tolerante a fallos basado en datos, tampoco de tiempo fijo.

En una tabla que clasifica arquitecturas por «cota independiente del estado inicial», esas dos entradas contradicen la columna que la fila marca como «Sí». **Propuesta:** dejar `\citep{Polyakov2012}` y, si se quiere acompañar, añadir `Ning2021` o `Huang2023`, que sí son de convergencia acotada.

### D1 · `Sowa2023` no es fuente sobre retardos ni pérdidas

`ANTECEDENTES.tex:45` — «los retardos de propagación y la pérdida estocástica de información son inherentes a los enlaces inalámbricos o redes cableadas compartidas `\citep{Sowa2023}`».

`Sowa2023` es *Distributed Consensus Control Supported by High Reporting Rate Meters in Inverter-Based Cyber-Physical Microgrids*: un controlador de consenso que **usa** mediciones de alta tasa. No documenta el comportamiento de la capa de red. **Propuesta:** mover la cita a la frase sobre medidores o sustituirla por `Olayanju2025ConsensusFreq`, que sí modela impedimentos.

### D2 · `Khanna2025` no es fuente sobre MQTT ni WebSockets

`ANTECEDENTES.tex:42` — «infraestructuras IoT y plataformas telemétricas ligeras como MQTT y WebSockets `\citep{Khanna2025}`».

Su resumen describe un marco multi-capa con pronóstico, optimización evolutiva y blockchain. No menciona MQTT ni WebSockets. **Es la tercera aparición del mismo problema** con esta clave: ya estaba en la frase de MQTT de la introducción (H16) y en el diagnóstico de la brecha. **Propuesta:** sustituir por `Diaz2025`, cuyo resumen sí trata arquitecturas de comunicación para controladores distribuidos.

### D3 · `AlvarezLopez2026` no documenta Raspberry Pi ni agentes en el borde

`ANTECEDENTES.tex:40` — «dispositivos como Raspberry Pi o microcontroladores industriales actúan como nodos inteligentes desalojados, alojando instancias individuales de los agentes `\citep{AlvarezLopez2026}`».

Es una revisión de IA para gestión energética en arquitecturas IoT-Edge-Cloud; no describe el despliegue físico concreto que la frase afirma. **Propuesta:** dejar la cita en la frase anterior —el paso a arquitecturas en el borde, que sí sostiene— y quitar el respaldo de la frase del hardware.

### D4 · `Zhang2024` y `Zhao2025` cierran una frase sobre el mecanismo propio

`ANTECEDENTES.tex:49` — «este trabajo incorpora esa dimensión temporal ausente mediante un desvanecimiento ponderado por la edad del último estado válido `\citep{Zhang2024, Zhao2025}`».

Se citan dos trabajos ajenos al final de la descripción de una contribución propia: ninguno propone ponderar por edad del dato. **Propuesta:** retirarlas de esa frase; la contribución se declara sin respaldo externo, como corresponde.

---

## Lo que sostiene solo una parte

| Sitio | Qué falla | Propuesta |
|---|---|---|
| `ANTECEDENTES.tex:9` — «consenso óptimo que combina **MPC** con *leader-follower* y *leaderless*» `\citep{Guo2026, Salman2024}` | Guo2026 sí unifica leaderless y leader-follower; Salman2024 es despacho óptimo por consenso. **Ninguno es MPC** | quitar «MPC» o decir «control óptimo» |
| `ANTECEDENTES.tex:42` — «los *brokers* imponen preservar la autonomía P2P» `\citep{Diaz2025, Mamun2026}` | Diaz2025 sostiene que las arquitecturas de comunicación quedan indefinidas; Mamun2026 describe retos de coordinación | aceptable; conviene añadir «según documentan» para no atribuirles la formulación exacta |
| `ANTECEDENTES.tex:47` — lista de observadores y aislamiento de enlaces `\citep{Barzegari2022Resilient, TaverasCruz2025, Fathima2024, Olayanju2025ConsensusFreq}` | los tres primeros sostienen observadores, protección y aislamiento; Olayanju2025 es control de frecuencia | retirar `Olayanju2025ConsensusFreq` de esa lista |

---

## Lo que quedó confirmado como pertinente

31 instancias, entre ellas las que sostienen el núcleo del capítulo: `SimpsonPorco2015` como origen de las leyes de promedio distribuido, `Khayat2020` y `Li2019` para la taxonomía de tres familias, `Polyakov2012` para el tiempo fijo, `Ning2021` para retardos, `Choi2022` para disparo por eventos, `Huang2023` para tiempo predefinido, `Amrr2026` para tiempo exacto, `Ge2021`, `Zhai2024` y `Huang2026TIE` para regulación de tensión y reactiva, y el bloque de co-simulación (`Gomes2022FMI30`, `Muszynski2026EnergyTwin`, `Liu2025Multirate`, `Haid2022CosimCorrector`, `Kyllingstad2025CosimErrors`).

Dos dudas provisionales se resolvieron a favor al leer el título completo: `Chen2024` sí es disparo por eventos («via dynamic event-triggered control») y `AlTameemi2024` sí es algoritmo de consenso por eventos, de modo que la frase de `ANTECEDENTES.tex:11` está bien apoyada.

---

## Reparaciones aplicadas (2026-11-08)

| ID | Cambio |
|---|---|
| N1 | Fila «tiempo fijo»: `\citep{Polyakov2012, Zhang2024, Zhao2025}` → `\citep{Polyakov2012, Huang2023}`, que sí es de convergencia con instante acotado |
| D1 | `Sowa2023` → `Olayanju2025ConsensusFreq` en la frase sobre retardos y pérdida de paquetes |
| D2 | `Khanna2025` → `Diaz2025` en la frase de MQTT y WebSockets |
| D3 | Retirada la cita de `AlvarezLopez2026` de la frase sobre Raspberry Pi y agentes en el borde |
| D4 | Retiradas `Zhang2024` y `Zhao2025` de la frase que describe el mecanismo propio |
| P1 | «teoría de control predictivo (MPC)» → «despacho económico», que es lo que `Salman2024` sostiene |
| P2 | «según documentan» antes de `\citep{Diaz2025, Mamun2026}`, para no atribuirles la formulación exacta |
| P3 | `Olayanju2025ConsensusFreq` fuera de la lista de observadores y aislamiento de enlaces |

### Limpieza de `Khanna2025`: siete apariciones revisadas

Era la cita comodín del documento. Su resumen —marco multi-capa con pronóstico, optimización evolutiva y blockchain— no respalda ninguna afirmación sobre MQTT, y sí el papel de marco multiagente.

| Sección | Frase | Decisión |
|---|---|---|
| Introducción | protocolo telemétrico MQTT | **retirada**: la frase describe la plataforma propia |
| Antecedentes | MQTT y WebSockets | **sustituida** por `Diaz2025` |
| Justificación | MQTT para perturbaciones y telemetría | **retirada** |
| Diseño | Actividad 2.3, canal MQTT e InfluxDB | **retirada**; queda `Diaz2025` |
| Teoría | canal asíncrono MQTT | **retirada**; quedan `Gomes2022FMI30, Diaz2025` |
| Introducción | marcos MAS que reducen el circuito | **conservada**: es un marco multiagente sin modelo eléctrico |
| Problema | idem, ítem b) | **conservada** |

`Khanna2025` queda con dos citas pertinentes en lugar de siete, y el `.bib` no pierde ninguna entrada.

### Verificación

`latexmk -pdf`: **79 páginas · 755 740 B · `1da0e21a…`**, 0 errores, 0 citas indefinidas, 0 avisos de BibTeX, sin `??`. Auditoría: **51 citadas / 51 entradas**, ninguna huérfana.

## Total a reparar

**4 retiros de cita** (D1–D4), **1 fila de tabla** con dos claves cambiadas (N1) y **3 ajustes de frase** en las parciales. Ninguno exige tocar el `.bib`: todas las claves siguen citadas en otros lugares.
