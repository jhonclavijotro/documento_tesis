# Informe de pertinencia — lote 3: Marco teórico

**Método.** Igual que los lotes anteriores: qué demuestra la fuente, después qué le atribuye la frase. 22 instancias de cita sobre 22 claves.

**Riesgo propio de este capítulo:** aquí las citas no acompañan contexto, respaldan ecuaciones, cotas y definiciones. Una cita que no sostiene la fórmula es más grave que una que no sostiene un párrafo de estado del arte.

**Resultado:** 13 pertinentes · 3 parciales · 3 dudosas · 1 no pertinente · 2 dudas resueltas a favor al leer el título completo.

---

## Lo que no corresponde

### T1 · `Alam2024` no define un modelo de gobernador diésel

`TEORIA.tex:101` — «Gobernador isócrono de velocidad con constante de tiempo del actuador $T_{act}$ y constante de transporte del motor térmico $T_{eng}$ `\citep{Alam2024}`».

`Alam2024` es *Renewable energy integration with DC microgrids: Challenges and opportunities*: una revisión de integración de renovables en microrredes DC. No contiene un modelo de gobernador con esas constantes. **Propuesta:** citar `Saadat2010`, que sí desarrolla el modelo de turbina-gobernador de velocidad, o `Glover2017`.

### T2 · `Kundu2024ICCFPLL` no es la fuente de la función de transferencia ni de las ganancias del PLL

`TEORIA.tex:40` — «La función de transferencia en lazo cerrado para pequeñas variaciones de ángulo $\Delta\theta$ es `\citep{Kundu2024ICCFPLL}`».
`TEORIA.tex:51` — «La selección de estos parámetros responde a un compromiso óptimo de diseño para sistemas a $60\ \text{Hz}$ `\citep{Kundu2024ICCFPLL}`».

El artículo propone un **ICCF-PLL**, no el SRF-PLL clásico cuya función de transferencia se escribe en la ecuación anterior. Y las ganancias $K_{p}=94.25$, $K_{i}=2220.66$ del manuscrito salen de $\zeta = 1.0$ y $\omega_n = 47.12$, que el propio capítulo calcula dos ecuaciones antes: son **una derivación del autor**, no un dato de esa referencia. **Propuesta:** declarar la ecuación como derivación propia a partir del modelo estándar y citar a Kundu solo para el contexto de PLL en generación distribuida.

### T3 · `Wang2022DataDriven` no es fuente sobre la estructura de las matrices de sensibilidad

`TEORIA.tex:130` — «las submatrices cruzadas $\mathbf{S}_{VP}$ y $\mathbf{S}_{fQ}$ son significativamente no nulas, reflejando el acoplamiento intrínseco `\citep{Pompodakis2022Sensitivity, Wang2022DataDriven}`».

`Pompodakis2022Sensitivity` sí establece las sensibilidades. `Wang2022DataDriven` es control de tensión basado en datos en redes con microrredes: no analiza la estructura de las submatrices. **Propuesta:** dejar `Pompodakis2022Sensitivity`; si se quiere conservar Wang, llevarla a la frase sobre control de tensión.

---

## Parciales

| Sitio | Qué falla | Propuesta |
|---|---|---|
| `TEORIA.tex:120` — «FBS especialmente formulado para topologías radiales `\citep{Glover2017}`» | Glover es un texto de análisis de sistemas de potencia que cubre flujo de carga en general; el FBS se atribuye habitualmente a la literatura de redes de distribución | citar `Pompodakis2022Sensitivity` o `DiFazio2024Linear` |
| `TEORIA.tex:154` — «se implementan cuatro lazos de consenso independientes que aplican la misma ley bi-potencia `\citep{Jasim2023, Zhuang2025}`» | los cuatro lazos son el diseño de **este** trabajo; Jasim y Zhuang proponen dos lazos (frecuencia y tensión) | quitar la cita de esa frase |
| `TEORIA.tex:250` — canal asíncrono MQTT para inyección exógena `\citep{Gomes2022FMI30, Diaz2025}` | Gomes es el estándar FMI y Diaz describe arquitecturas IoT; ninguno documenta inyección de perturbaciones por MQTT | dejar solo `Diaz2025` o ninguna, por tratarse de la plataforma propia |

---

## Dudas resueltas a favor

- **`Zhuang2025`** — el título completo es *Distributed Optimal Secondary Control of Microgrids: A Consensus-Driven Hierarchical Algorithm With **Predefined** Time*: sí sostiene la frase de tiempo predefinido. La instancia de `TEORIA.tex:140` queda validada con sus tres citas.
- **`Kundu2024ICCFPLL`** en `TEORIA.tex:28` — el artículo implementa control `dq` y un PLL en un sistema de generación distribuida: la cita de las transformadas de Clarke y Park es pertinente. Lo que no sostiene son las dos instancias siguientes (T2).

## Pertinentes confirmadas (13)

`Saadat2010` para la ecuación de oscilación · `Mehrzad2025` para inercia y RoCoF · `Jasim2023` para los coeficientes de estatismo · `Kundu2024ICCFPLL` para `dq0` · `Pompodakis2022Sensitivity` para $R/X \ge 1$ y las sensibilidades · `DiFazio2024Linear` para el barrido hacia adelante · `Shrivastava2023FiniteTime`, `Ning2021` y `Choi2022` para la dependencia de la cota respecto de $x(0)$ · `Polyakov2012` para los exponentes duales · `Jasim2023` y `Zhuang2025` como aplicaciones al control secundario · `Mamun2026` para la matriz de adyacencia · `Shrivastava2023FiniteTime` para $\mathcal{H} = \mathcal{L} + \mathcal{B}$ · `Liu2025Multirate` y `Haid2022CosimCorrector` para el esquema multirate · `Kyllingstad2025CosimErrors` para el error de acoplamiento explícito.

---

## Verificación numérica previa a la reparación de T2 (2026-11-08)

Antes de declarar la sintonización del PLL como derivación propia se recomputó todo con `verificar_pll.py`:

| Magnitud | Valor recomputado | Lo que publica el capítulo |
|---|---|---|
| $\omega_n = 2\pi \cdot 7.5$ | $47.123890\ \text{rad/s}$ | $47.1239$ ✓ |
| $K_p = 2\zeta\omega_n/V_{\text{pico}}$ | $94.24778$ | $94.25$ ✓ |
| $K_i = \omega_n^2/V_{\text{pico}}$ | $2220.661$ | $2220.66$ ✓ |
| Polos del lazo cerrado | $-47.12\ \text{rad/s}$, real doble | amortiguamiento crítico ✓ |
| $t_s$ banda $5\%$ | $100.7\ \text{ms}$ | $\approx 100\ \text{ms}$ ✓ |
| $t_s$ banda $2\%$ | $123.8\ \text{ms}$ | $124\ \text{ms}$ ✓ |
| Atenuación a $120\ \text{Hz}$ | $-18.1\ \text{dB}$ (factor $0.125$) | $-18.1\ \text{dB}$, factor $0.125$ ✓ |
| Margen de fase del lazo | $76.3^\circ$ a $15.44\ \text{Hz}$ | no declarado, coherente con $\zeta = 1$ |

**Veredicto:** las ecuaciones y todos los valores entregados son correctos y mutuamente consistentes. El problema de T2 era **solo de atribución**, no de veracidad: el capítulo citaba a `Kundu2024ICCFPLL` una función de transferencia estándar y una sintonización que él mismo deriva dos ecuaciones antes.

## Reparaciones aplicadas

| ID | Cambio |
|---|---|
| T1 | Gobernador diésel: `Alam2024` → `Saadat2010`, que sí desarrolla el modelo turbina-gobernador |
| T2a | `Kundu2024ICCFPLL` pasa a acompañar el contexto del PLL en generación distribuida; la ecuación queda como formulación estándar del lazo |
| T2b | La frase del compromiso de diseño deja de citar a Kundu y declara el criterio propio, con las cifras ya verificadas ($100\ \text{ms}$, $18.1\ \text{dB}$) |
| T3 | `Wang2022DataDriven` retirada de la frase de sensibilidades; al quedar huérfana se retiró del `.bib`: **50 entradas** |
| P1 | «cuatro lazos» deja de atribuirse a `Jasim2023, Zhuang2025` |
| P2 | Canal MQTT: queda solo `Diaz2025`; `Gomes2022FMI30` ya se cita antes |

`Glover2017` como fuente del FBS se mantiene: es un texto de análisis de sistemas de potencia que cubre el flujo de carga en distribución, y retirarla dejaría huérfano un libro legítimo.

### Verificación

`latexmk -pdf`: **79 páginas · 755 004 B · `c11375ea…`**, 0 errores, 0 citas indefinidas, 0 avisos de BibTeX, sin `??`. Auditoría: **50 citadas / 50 entradas**.

## Total a reparar

**1 sustitución de fuente** (T1), **2 atribuciones que deben pasar a derivación propia** (T2), **1 retiro** (T3), **3 ajustes de frase** en las parciales. Ninguna clave queda huérfana salvo `Wang2022DataDriven` si se retira del todo, que exige recolocarla en la frase de control de tensión.
