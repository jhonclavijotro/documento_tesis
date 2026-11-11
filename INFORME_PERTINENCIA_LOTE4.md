# Informe de pertinencia — lote 4: Diseño metodológico e Implementación

**Método.** Igual que los lotes anteriores. 21 instancias (8 en Diseño, 13 en Implementación) sobre las claves ya verificadas contra CrossRef en el bloque de bibliografía.

**Resultado:** 8 pertinentes · 6 parciales o dudosas · **4 no pertinentes** · 3 de las 4 son repeticiones de defectos ya corregidos en otros capítulos.

---

## No pertinentes

### C1 · `AlvarezLopez2026` otra vez, ahora para el hardware — dos sitios

- `DISENO.tex:34` — «Despliegue del clúster de microcomputadores embebidos (Raspberry Pi 5) actuando como nodos de generación distribuidos `\citep{AlvarezLopez2026}`».
- `IMPLEMENTACION.tex:171` — «…a través de una red Ethernet dedicada con switch propio `\citep{AlvarezLopez2026}`».

Es una revisión de IA para gestión energética en IoT-Edge-Cloud. **No documenta un despliegue concreto ni una red Ethernet con switch dedicado.** Es el mismo defecto que se retiró en Antecedentes (D3) y que reaparece aquí dos veces.

**Propuesta:** retirar la cita en ambos sitios; la Actividad 3.1 y la descripción de la red del clúster son decisiones de ingeniería propias.

### C2 · `Barzegari2022Resilient` no define las métricas

`DISENO.tex:44` — lista de métricas (RMSE, $T_{set}$, nadir, RoCoF, índices de reparto, $\tau_{crit}$) `\citep{Barzegari2022Resilient}`.

Es detección de inyección de datos falsos con observadores de modos deslizantes. Las definiciones formales están en `TEORIA` (`eq:rmse`, `eq:tset_band`, `eq:tau_crit`, `eq:share_index`), y la propia actividad remite a ellas con `\eqref`. **Propuesta:** retirar la cita; la remisión a las ecuaciones es el respaldo correcto.

### C3 · `Alam2024` no modela el generador diésel — segundo sitio

`IMPLEMENTACION.tex:101` — «actuando como generador síncrono formador de red (*Grid-Forming*) en modo isla `\citep{Alam2024}`».

Ya se corrigió en `TEORIA.tex:101` (T1 del lote 3) cambiando la cita a `Saadat2010`. Aquí queda la misma atribución. **Propuesta:** `\citep{Saadat2010}`.

### C4 · `Zhang2024` y `Zhao2025` no proponen la política de edad del dato

`IMPLEMENTACION.tex:137` — «se implementa una política de desvanecimiento dinámico de enlaces basada en la edad del estado recibido `\citep{Zhang2024, Zhao2025}`».

Es la contribución propia del trabajo. Se corrigió en `ANTECEDENTES` (D4) pero sobrevive aquí. **Propuesta:** retirar ambas citas de esta frase.

---

## Parciales y dudosas

| Sitio | Qué falla | Propuesta |
|---|---|---|
| `DISENO.tex:19` — ley en tiempo fijo, Lyapunov y capa anti-chattering `\citep{Shrivastava2023FiniteTime, Guo2026}` | Shrivastava sí es tiempo finito; Guo2026 es consenso óptimo y no trata anti-chattering | dejar `Shrivastava2023FiniteTime` |
| `DISENO.tex:27` — temporizadores ZeroMQ (`RCVTIMEO`, `SNDTIMEO`, `LINGER`) `\citep{Gomes2022FMI30}` | Gomes es el estándar FMI 3.0; los valores de *timeout* son decisiones de implementación | retirar la cita |
| `DISENO.tex:28` — MQTT e InfluxDB a 500 ms `\citep{Diaz2025}` | Diaz describe arquitecturas IoT y señala que la capa de comunicación suele quedar indefinida | aceptable |
| `DISENO.tex:43` — envolvente de fallas (50–500 ms, 0–30 %, partición) `\citep{Sowa2023, Olayanju2025ConsensusFreq}` | ninguno define esa envolvente; la eligen las actividades 4.2 del propio diseño | aceptable como contexto, conviene matizar |
| `IMPLEMENTACION.tex:22` — conmutación ONLINE/OFFLINE `\citep{MartinezGomez2025Distributed}` | es control distribuido de microrredes múltiples; no describe esa conmutación | dudosa: verificar o retirar |
| `IMPLEMENTACION.tex:37` — «teorema de consistencia numérica para co-simulación explícita demostrado por `\citet{Kyllingstad2025CosimErrors}`» | el artículo analiza errores por cambio de tamaño de paso; llamarlo teorema es más de lo que el trabajo establece | rebajar a «el análisis de error de …» |
| `IMPLEMENTACION.tex:86` — control `dq` en el punto de conexión a 400 V `\citep{Kundu2024ICCFPLL}` | verosímil, pero la tensión de 400 V es del banco propio | aceptable |

## Pertinentes confirmadas (8)

`Kundu2024ICCFPLL` para las cinco tipologías con `dq` y PLL · `Liu2025Multirate`, `Kyllingstad2025CosimErrors` y `Haid2022CosimCorrector` para el acoplamiento multirate con $N_{substeps}=500$ · `Mamun2026` y `Altin2023MultiAgent` para el intercambio asíncrono sin controlador central · `Shrivastava2023FiniteTime` para el seguimiento de líder · `DiFazio2024Linear` para el barrido hacia adelante · `Pompodakis2022Sensitivity` para la linealización por jacobiano reducido · `Sowa2023` y `Olayanju2025ConsensusFreq` para la inyección de fenómenos estocásticos.

---

## Total a reparar

**5 retiros de cita** (C1 ×2, C2, C4, más el temporizador de `DISENO:27`), **1 sustitución** (C3 → `Saadat2010`) y **1 rebaja de afirmación** (el «teorema» de Kyllingstad). Las claves afectadas siguen citadas en otros capítulos, salvo comprobación puntual, de modo que el `.bib` no debería moverse de 50 entradas.

## Observación de cierre de los cuatro lotes

Con este lote quedan **100 instancias** revisadas. El patrón se repite con precisión: las fuentes existen y son pertinentes **al tema**, pero en 8 casos respaldan una frase que no les corresponde, y **cuatro de esos defectos ya se habían corregido en otro capítulo y reaparecen aquí**. Eso indica que la revisión por secciones no basta: el último paso debería ser un barrido transversal sobre las cuatro o cinco claves problemáticas (`AlvarezLopez2026`, `Alam2024`, `Zhang2024`/`Zhao2025`, `Barzegari2022Resilient`, `Gomes2022FMI30`) para asegurar que el defecto no sobrevive en ninguna otra frase.
