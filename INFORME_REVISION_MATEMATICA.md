# Informe de revisión matemática — Tesis MAS-Microgrid

**Fecha:** 2026-11-02 · **Alcance:** `main.tex` + 8 secciones · 762 líneas · 48 ecuaciones etiquetadas
**Método:** lectura completa, recálculo de cada cifra publicada con la ecuación del propio documento, contraste con `Agents/finite_time_consensus.py`, y auditoría estructural con los scripts de la skill.
**Estado de compilación:** 48 páginas · 405.555 bytes · 0 errores · 0 referencias indefinidas · 0 citas indefinidas · 0 BibTeX.

---

## Resumen por severidad

**Estado a 2026-11-02, tras tres tandas de corrección:** 9 de 17 cerrados · 50 páginas · 409.444 bytes · 0 errores · 0 referencias indefinidas · 0 citas indefinidas · 0 warnings de caja.

**Estado a 2026-11-04, cierre final:** **17 de 17 cerrados** · 51 páginas · 413.041 bytes · 0 errores · 0 referencias indefinidas · 0 citas indefinidas · 1 overfull (encabezado de la tabla comparativa de `ANTECEDENTES.tex`, preexistente).

| # | Hallazgo | Ubicación | Severidad | Estado |
|---|---|---|---|---|
| M-01 | $c_1 = c_2 = 1.0$ contradice $c_1{=}0.25$, $c_2{=}0.15$ de la teoría | `IMPLEMENTACION.tex:109` | **Crítica** | ✅ **Corregido** |
| M-02 | El régimen de exponentes está invertido en el párrafo de justificación | `TEORIA.tex:218` | **Crítica** | ✅ **Corregido** |
| M-03 | Atribución de régimen a los exponentes | `TEORIA.tex:167` vs `218` | **Crítica** | ✅ **Corregido** (con M-02) |
| M-04 | La atenuación del PLL a 120 Hz es −18.1 dB, no «superior a −24 dB» | `TEORIA.tex:52` | Alta | ✅ **Corregido** |
| M-05 | La CFL publicada ignora la pendiente de la zona muerta $k_p = 3.981$ | `TEORIA.tex:216` | Alta | ✅ **Corregido** |
| M-06 | La introducción declara seis secciones y hay siete | `INTRODUCCION.tex:14` | Alta | ✅ **Corregido** |
| M-07 | El modo OFFLINE enumera 4 seguidores: implica 5 agentes, no 3 | `IMPLEMENTACION.tex:24` | Alta | ✅ **Corregido** |
| M-08 | $\varepsilon$ designa la zona muerta y la banda con símbolos casi idénticos; y la cifra de $T_{set}$ se calculó con otra banda | `TEORIA.tex:205, 218, 262` | **Alta** | ✅ **Corregido** (M-08a + M-08b; M-08c descartado) |
| M-09 | La banda de $T_{set}$ del 2 % coincide con el umbral de protección | `TEORIA.tex:262` | Media | ✅ **Corregido** |
| M-10 | $k_p$ se publica solo para $\alpha$; el operador se aplica a $\beta$ también, y `\gamma` quedaba indefinida | `TEORIA.tex:209, 218` | Media | ✅ **Corregido** |
| M-11 | La ecuación de frescura nunca llega a 0, pero el texto y el código excluyen | `IMPLEMENTACION.tex:130-132` | Media | ✅ **Corregido** |
| M-12 | $T_{\max}$ y $T_f$ designaban la misma cota | `DISENO.tex:12`, `TEORIA.tex:199` | Media | ✅ **Corregido** |
| M-13 | Frase huérfana que anuncia índices que no siguen | `ANTECEDENTES.tex:24` | Media | ✅ **Corregido** |
| M-14 | $K_{i,\text{pll}} = 2220.0$; el valor exacto es 2220.66 | `TEORIA.tex:46-47`, `IMPLEMENTACION.tex:79`, `DISENO.tex:11` | Baja | ✅ **Corregido** |
| M-15 | Los 6.8 kvar no se derivaban de ninguna parte | `IMPLEMENTACION.tex:105` | Baja | ✅ **Corregido** |
| M-16 | $t_s = 4.75/\omega_n$ es la banda del 5 %, sin declararla | `TEORIA.tex:53`, `DISENO.tex:11` | Baja | ✅ **Corregido** |
| M-17 | Errores de concordancia | `PROBLEMA.tex:19`, `JUSTIFICACION.tex:18`, `INTRODUCCION.tex:6` | Baja | ✅ **Corregido** |

### Registro de las correcciones aplicadas

| Hallazgo | Cambio exacto | Verificación |
|---|---|---|
| M-01 | `c_1 = 1.0` y `c_2 = 1.0` → `c_1 = 0.25` y `c_2 = 0.15` | 0 apariciones del viejo; `c1 = 0,25` y `c2 = 0,15` tres veces cada uno en el PDF |
| M-02 | «acelera la fase de error grueso, gobernada por $\alpha<1$» → «la acción de control crece en la región $\lvert e\rvert<1$ —gobernada por $\alpha<1$—, que es donde se ubican las desviaciones de operación» | «error grueso» = 0; cifras 10.5 · 17.0 · 32 · 22.5 · 0.207 · 0.193 · 50.06 intactas |
| M-04 | «superior a $-24\text{ dB}$» → «$-18.1\text{ dB}$ (factor $0.125$)» | `-18,1 dB` en el PDF; `24 dB` = 0; $f_n$, $K_p$, $K_i$ sin tocar |
| M-05 | CFL reformulada sobre el espectro: $\Delta t\,\lambda_{\max}(\mathcal{H})\,g_{ef}<2$ con $g_{ef}$ por régimen; 4 sitios coordinados | $1{,}677$ · $16{,}2\,\%$ · $67{,}5\,\%$ · $3{,}247$ · $161$ ms · $0{,}677$ en el PDF; «margen del 60» = 0 |
| M-06 | «seis» → «siete» + ítem de Arquitectura e Implementación | 19/19 cadenas del original intactas; 22 → 23 líneas, una añadida |
| M-07 | Enumera 4 seguidores → «seguidores de la topología activa» + «admite hasta cinco recursos (…) la validación emplea la configuración reducida de tres agentes» | `(Solar, Eólica, BESS, Hídrica)` = 0; `\citep{Shrivastava2023FiniteTime}` conservado |
| M-09 | Declaración de $T_{set}$ como **métrica de protección**: la banda del 2 % sobre 60 Hz es $\pm1.2$ Hz, idéntica al umbral NTC 1340 | $\varepsilon = 0.02$ **sin cambios** (umbral normativo intacto); declaración explícita presente |
| M-11 | Explicación en dos etapas: desvanecimiento con piso 0.20 y **exclusión dura** por borrado del búfer | «dos etapas complementarias» · «piso de 0,20» · «exclusión dura» presentes; texto fundido = 0 |
| M-13 | Eliminada la frase huérfana y su línea en blanco | 11/11 cadenas de la sección intactas; una sola línea en blanco antes del `\subsection` |

### Consecuencias de M-05 sobre cifras del documento

| Cantidad | Antes | Ahora |
|---|---|---|
| Margen numérico declarado | 60 % | **16.2 %** (régimen que gobierna) · 67.5 % fuera de la capa límite |
| Retardo crítico teórico | no se publicaba | **$\tau < 161$ ms** |
| Ecuación de la condición | $\Delta t\,d_{\max}(c_1{+}c_2)<1$ | $\Delta t\,\lambda_{\max}(\mathcal{H})\,g_{ef}<2$ |

$\lambda_{\max}(\mathcal{H}) = 3.247 < 2d_{\max} = 4$: por eso la forma con $d_{\max}$ daba un falso positivo de inestabilidad (1.033 > 1) mientras el esquema converge. El modo crítico decae con factor 0.677 por paso y solo se activa para $\lvert e\rvert \le 10^{-3}$.

Los tres primeros son los que un jurado encuentra en los primeros diez minutos.

## M-01 · Los parámetros del controlador se contradicen entre capítulos

`IMPLEMENTACION.tex:109` dice:

> «Cada agente ejecuta la ley de control no lineal bi-potencia (…) con parámetros nominales sintonizados $\alpha = 0.8$, $\beta = 1.2$, **$c_1 = 1.0$ y $c_2 = 1.0$**.»

`TEORIA.tex:200` y `TEORIA.tex:218` dicen $c_1 = 0.25$, $c_2 = 0.15$.

**No es un detalle de estilo: las dos parejas producen tesis distintas.**

| | $c_1{=}0.25$, $c_2{=}0.15$ | $c_1{=}c_2{=}1.0$ |
|---|---|---|
| Cota $T_f$ | **52.54 s** | **10.02 s** |
| CFL con $\Delta t{=}0.5$, $d_{\max}{=}2$ | 0.40 ✅ | **2.00 ❌ inestable** |
| Comportamiento | converge monótono | **oscila** (23 cruces medidos) |

El valor 1.0/1.0 es el *default* de la librería (`finite_time_consensus.py:89-90`) y **no pasa la verificación CFL del propio código**: `verify_discrete_cfl_stability(0.5, 2)` devuelve `(False, 2.0, 0.25)`. El runner del proyecto lo sobrescribe con 0.25/0.15, que es lo que la teoría declara.

**La aritmética delata cuál está mal:** la cota publicada de 52.54 s solo se reproduce con 0.25/0.15. Con 1.0/1.0 daría 10.02 s. El párrafo defectuoso es el de implementación.

**Riesgo en defensa:** es la primera cifra que un jurado contrasta entre dos capítulos.

---

## M-02 y M-03 · El régimen de exponentes está invertido

`TEORIA.tex:167` afirma correctamente:

> «$\text{sig}^\alpha$ ($\alpha = 0.8 < 1$) domina (…) cuando el error se encuentra **próximo al origen** ($|e| < 1$), mientras que $\text{sig}^\beta$ ($\beta = 1.2 > 1$) proporciona rápida tasa de rechazo ante perturbaciones de **gran magnitud** ($|e| > 1$).»

`TEORIA.tex:218` —el párrafo de justificación añadido hoy— afirma lo contrario:

> «(…) porque ponderar $c_1 > c_2$ acelera la **fase de error grueso, gobernada por el exponente $\alpha < 1$**.»

**Verificación numérica:**

| $\lvert e\rvert$ | $\lvert e\rvert^{0.8}$ | $\lvert e\rvert^{1.2}$ | Domina |
|---|---|---|---|
| 0.01 | 0.02512 | 0.00398 | **$\alpha$** |
| 0.10 | 0.15849 | 0.06310 | **$\alpha$** |
| 0.50 | 0.57435 | 0.43528 | **$\alpha$** |
| 1.00 | 1.00000 | 1.00000 | igual |
| 2.00 | 1.74110 | 2.29740 | **$\beta$** |
| 10.0 | 6.30957 | 15.84893 | **$\beta$** |

$\alpha$ gobierna la región **cercana al origen**, no el error grueso.

**Consecuencia:** con $c_1 > c_2$ la acción de control es **mayor para $|e|<1$** y menor para $|e|>1$:

| $\lvert e\rvert$ | Tesis 0.25/0.15 | Balanceada 0.207/0.193 | Más fuerte |
|---|---|---|---|
| 0.10 | 0.04909 | 0.04498 | tesis |
| 0.40 | 0.17007 | 0.16371 | tesis |
| 0.80 | 0.32389 | 0.32081 | tesis |
| 1.50 | 0.58980 | 0.60029 | balanceada |
| 2.00 | 0.77988 | 0.80386 | balanceada |

Como las desviaciones de una microrregla viven en $|e| < 1$ pu, la pareja asimétrica aplica más acción **en todo el recorrido útil** — y eso explica el 10.5 % de ventaja medido, no una supuesta ventaja en el régimen de error grueso.

**La conclusión es válida; la explicación está al revés.** Corregir la frase, no las cifras.

---

## M-04 · La atenuación del PLL no alcanza el valor declarado

`TEORIA.tex:52` afirma:

> «Al fijar $f_n = 7.5\text{ Hz} \ll 120\text{ Hz}$, el filtro pasobajas intrínseco del lazo cerrado proporciona una **atenuación superior a −24 dB** en dicha componente.»

Con la función de transferencia del propio documento (`eq:pll_tf`), $\zeta = 1$, $\omega_n = 47.12$ rad/s, evaluada en $\omega = 2\pi\cdot120 = 754$ rad/s:

$$\left|H_{cl}(j\omega)\right| = \frac{\left|\omega_n^2 + j2\zeta\omega_n\omega\right|}{\left|\omega_n^2-\omega^2 + j2\zeta\omega_n\omega\right|} = \frac{71094}{570710} = 0.1246$$

$$20\log_{10}(0.1246) = \mathbf{-18.09\ dB}$$

**−18.1 dB, no −24 dB.** Para alcanzar −24 dB con este lazo haría falta $f_n \approx 3.79$ Hz, no 7.5 Hz.

La conclusión cualitativa (rechazo suficiente de la componente de secuencia negativa) se mantiene; la cifra no.

---

## M-05 · La condición CFL publicada no es la que gobierna

`TEORIA.tex:216` publica:

$$\Delta t \cdot d_{\max} \cdot (c_1 + c_2) < 1.0 \;\Rightarrow\; 0.5 \times 2 \times 0.40 = 0.40$$

Pero el operador anti-chattering (`eq:anti_chattering`, línea 207) **linealiza la ley cerca del origen** con pendiente $k_p = \varepsilon^{\gamma-1}$. Para $\alpha = 0.8$: $k_p = (10^{-3})^{-0.2} = 3.981$ — diez veces la ganancia.

La rigidez efectiva en la región lineal es:

| Supuesto | Rigidez $c_1k_{p,\alpha} + c_2k_{p,\beta}$ | CFL efectiva |
|---|---|---|
| $k_p$ única (3.981 para ambos) | 1.5924 | **1.5924** ❌ |
| $k_p$ por exponente (3.981 y 0.251) | 1.0329 | **1.0329** ❌ |

**La CFL real en la zona muerta es 1.033, no 0.40, y excede el límite de 1.0 que el propio documento publica.**

El sistema **no** diverge — el criterio real de Euler explícito es $\Delta t\lambda < 2$, y aquí da 1.033 — pero entonces el documento publica una condición que su propio mecanismo de suavizado no cumple. Dos salidas:

1. Reformular la CFL incorporando $k_p$ y **elevar el umbral a 2**, que es el criterio correcto de Euler.
2. Declarar que la CFL aplica sobre la región no lineal ($|e| > \varepsilon$) y que la zona muerta se verifica aparte.

Ninguna de las dos se deduce del texto actual.

---

## M-06 · La introducción anuncia seis secciones y hay siete

`INTRODUCCION.tex:14`: «El documento de tesis se encuentra estructurado en **seis** secciones fundamentales».

El listado enumera: Problema · Objetivos · Justificación · Antecedentes · Marco Teórico · Diseño Metodológico = **6**.

`main.tex` incluye **7 secciones numeradas** (sin contar PORTADA ni la propia INTRODUCCIÓN). La que falta en la lista es **«Arquitectura e Implementación del Sistema Multiagente y Co-Simulación»** — la sección más extensa del documento (171 líneas, 22 KB), precisamente donde está el aporte instrumental de la tesis.

El jurado ve el índice completo de siete entradas y una introducción que anuncia seis.

---

## M-07 · El modo OFFLINE describe cinco agentes donde hay tres

`IMPLEMENTACION.tex:24`:

> «El protocolo de seguimiento de líder propaga ambas consignas de restauración hacia los inversores seguidores **(Solar, Eólica, BESS, Hídrica)**».

Cuatro seguidores + el diésel como líder = **5 agentes de consenso**.

Pero `TEORIA.tex:142` y `TEORIA.tex:200` fijan $N_{\text{DER}} = 3$ (diésel, solar, BESS), y `OBJETIVOS.tex:12` confirma la configuración de validación con tres recursos. El modelo contempla cinco tipologías, pero la validación usa tres.

Falta la acotación: el texto describe la arquitectura general como si fuera la topología validada.

---

## M-08 · Notación del épsilon: dos defectos reales y uno descartado

**Diagnóstico inicial (2026-11-02):** «el símbolo $\varepsilon$ designa tres cantidades distintas».

**Revisión del 2026-11-04:** parcialmente correcto. Se descompone en tres, y solo dos sobreviven.

| | Qué era | Veredicto |
|---|---|---|
| **M-08a** | `TEORIA.tex:218` publicaba $T_{set}=17.0$ s a $\varepsilon = 0.5\%$, mientras `:262` define la banda en $\varepsilon = 0.02$ | ✅ **Corregido** — el defecto grave |
| **M-08b** | `\epsilon = 10^{-3}` (zona muerta) y `\varepsilon` (banda) convivían en la línea 218 sin subíndice | ✅ **Corregido** — zona muerta renombrada a $\delta$ |
| **M-08c** | `\varepsilon_{\text{ZOH}}` colisionaba con la banda | ❌ **Descartado** — el subíndice desambigua |

### M-08a · La cifra de $T_{set}$ se calculó con una banda que la ecuación no define

`eq:tset_band` usa $\varepsilon$ como banda y `:262` la fija en $0.02$. Pero `:218` la evaluaba con $0.5\%$ —cinco veces más estrecha— y publicaba el resultado como si correspondiera a la definición.

Recalculado con el montaje que reproduce **exactamente** las cifras que el texto ya publicaba a $\varepsilon = 0.005$ (17.0 s y 22.5 s), a $\varepsilon = 0.02$:

| Magnitud | Publicado | Correcto |
|---|---|---|
| $T_{set}$ de la tesis | 17.0 s (32 % de la cota) | **13.5 s (26 %)** |
| Pareja invertida $c_1{=}0.15$, $c_2{=}0.25$ | 22.5 s | **17.5 s** |
| Balanceado $0.207/0.193$ frente al asimétrico | 10.5 % más lento | **11.1 % más lento** |

**Verificado en el PDF compilado:** las tres cifras nuevas presentes una vez cada una, las tres viejas ausentes.

**Nota sobre el 10.5 %.** No se reprodujo exactamente con ningún montaje: a $\varepsilon=0.005$ da 11.8 % y a $\varepsilon=0.02$ da 11.1 %. El 11.1 % es correcto para la banda vigente; el original no era reproducible, así que este cambio es una re-derivación, no un desplazamiento.

### M-08b · La zona muerta se renombró a $\delta$

Once ocurrencias de `\epsilon` en `TEORIA.tex` (L205; L207 ×2 en `eq:anti_chattering`; L209; L218 ×7) renombradas a `\delta`, más una frase declarativa en L205 que liga la distinción a `eq:tset_band`.

Se eligió $\delta$ por dos razones: es el símbolo convencional del espesor de capa límite en control discontinuo, y en el manuscrito no aparecía desnudo —solo como `\delta V_i` y `\delta \omega_i`—, así que no colisiona con nada.

| Símbolo | Antes | Después |
|---|---|---|
| `\epsilon` (zona muerta) | 11 | **0** |
| `\delta` | 4 (solo los incrementos integrales) | **16** |
| `\varepsilon` (banda) | 5 | **6** (5 + 1 de la frase nueva) |

**No se tocó** la `\gamma` de `TEORIA.tex:218` (`k_p = \delta^{\gamma-1}`): es **M-10** y se resuelve aparte. Arreglarla aquí habría mezclado dos hallazgos.

---

## M-09 · La banda de $T_{set}$ es el umbral de protección

Con $\varepsilon = 0.02$:

| Variable | Consigna | Banda resultante | Umbral NTC 1340 |
|---|---|---|---|
| Frecuencia | 60 Hz | **±1.2 Hz** | ±2 % = **±1.2 Hz** |
| Tensión | 1.0 p.u. | **±0.020 p.u.** | ±5 % = ±0.05 p.u. |

Para frecuencia, la banda del 2 % **coincide exactamente con el límite de protección**. Es decir: $T_{set}$ mide cuándo la señal entra en la banda en la que el relé de subfrecuencia ya habría actuado.

Un objetivo de control secundario se reporta a ±0.1 Hz (diez veces más estrecho que la norma). El documento necesita declarar que $T_{set}$ al 2 % es una **métrica de protección**, no de calidad de control, o publicar además $T_{set}$ a ±0.5 %.

Esto enlaza con la distinción que el propio `IMPLEMENTACION.tex:125` hace bien para las tres bandas de frecuencia: allí se separan correctamente los ±0.5 Hz del saturador, los ±2 % de la NTC 1340 y los [57, 63] Hz del relé ANSI 81. Esa triple distinción no se traslada a la definición de $T_{set}$.

---

## M-10 · La pendiente de empalme se publicaba solo para un exponente

`TEORIA.tex:209`:

> «la pendiente de empalme suave en la frontera satisface $k_p = \epsilon^{\alpha-1} = (10^{-3})^{-0.2} \approx 3.981$»

Pero el operador $\text{sig}^p$ se aplica **también** con $\beta = 1.2$ (línea 207, y el código lo hace con `sig_pow(y, gamma, epsilon)` calculando `k_p = epsilon ** (gamma - 1)` por exponente). Para $\beta$:

$$k_{p,\beta} = (10^{-3})^{1.2-1} = (10^{-3})^{0.2} = \mathbf{0.2512}$$

**Quince veces menor que la de $\alpha$.** La ecuación (209) sugería una única $k_p$ universal, lo que además induce el error de M-05 si alguien verifica la CFL con 3.981 para ambos términos.

Y en `TEORIA.tex:218` la pendiente se escribía $k_p = \delta^{\gamma-1}$, con una $\gamma$ **que no se define en ninguna parte del documento** y que aparecía una sola vez en todo el manuscrito.

### Corrección aplicada

| Línea | Antes | Después |
|---|---|---|
| 209 | $k_p = \delta^{\alpha-1} = 3.981$ | $k_p = \delta^{p-1}$, con **ambas**: $3.981$ ($\alpha$) y $0.251$ ($\beta$) |
| 218 | $k_p = \delta^{\gamma-1}$ | $k_p = \delta^{p-1}$ — la $p$ que ya usa $\text{sig}_k^p(z)$ |

No fue un error de cálculo: la cifra de $\beta$ ya se usaba veinte palabras después en $g_{\text{ef}} = c_1\delta^{\alpha-1} + c_2\delta^{\beta-1}$. Solo no se publicaba donde se define la pendiente.

**Verificado en el PDF:** $k_p = \delta^{p-1}$ con $3{,}981$ y $0{,}251$ en la misma frase; $\gamma$ = 0 ocurrencias en el fuente; $g_{\text{ef}} = 1{,}033$, CFL $1{,}677 < 2{,}0$, margen $16{,}2\,\%$ y $67{,}5\,\%$ sin cambios.

---

## M-11 · La ecuación de frescura no puede llegar a cero

`IMPLEMENTACION.tex:130` publica:

$$a_{ij}^{\text{efectivo}}(t) = a_{ij}\cdot\max\left(0.20,\; 1.0 - \frac{\text{stale\_steps}}{\text{max\_stale\_steps}+1}\right)$$

Con `max_stale_steps = 4`, el mínimo del segundo factor es $\max(0.20, 1-4/5) = \mathbf{0.20}$.

Pero `IMPLEMENTACION.tex:132` afirma que al superar el umbral «el agente excluye temporalmente el enlace de la matriz de adyacencia local ($a_{ij}^{\text{efectivo}} \to 0$)».

**La ecuación nunca vale 0; el texto dice que sí.** Lo que hace el código (`finite_time_consensus.py:143-149`) es **eliminar el vecino del búfer**, tras lo cual `update_consensus` lo salta con `if weight <= 0 or n_id not in self.neighbor_buffer: continue`. La exclusión es un borrado, no un peso nulo.

La ecuación describe la fase de decaimiento; falta la regla de exclusión dura que la sigue.

---

## M-12 · Dos símbolos para la misma cota

| Ubicación | Símbolo | Uso |
|---|---|---|
| `TEORIA.tex:138` | $T_{\max}$ | Correcto: rótulo de la clase FxTS en la taxonomía |
| `ANTECEDENTES.tex:6` | $T_{\max}$ | Se refiere a la cota de **este** trabajo |
| `DISENO.tex:12` | $T_{\max}$ | «calculando la cota superior (…$T_{\max}$)» |
| `TEORIA.tex:183-218` | $T_f$ | La cota del trabajo, 52.54 s |

`DISENO.tex:12` decía $T_f$: es la actividad de deducción de la cota propia, no una referencia a la clase.

### Corrección aplicada

| Edición | Ubicación | Cambio |
|---|---|---|
| 1 | `DISENO.tex:12` | `($T_{\max}$)` → **`($T_f$)`** |
| 2 | `TEORIA.tex:199` | Frase que declara la distinción una sola vez |

> «Aquí $T_f$ denota la cota específica de este trabajo, obtenida al evaluar \eqref{eq:t_settling} con los parámetros propios de diseño, en contraste con el límite genérico $T_{\max}$ que define la clase de estabilidad en tiempo fijo.»

Se conservó el $T_{\max}$ de `TEORIA.tex:138` (definición de la clase FxTS) y el de `ANTECEDENTES.tex:6` (convención de Polyakov 2012). Ahora los dos símbolos conviven con una regla explícita en lugar de por costumbre.

---

## M-13 · Frase huérfana en el estado del arte

`ANTECEDENTES.tex:24`:

> «Con el fin de evaluar la calidad del reparto proporcional de potencia, se definen los índices de utilización de cada unidad:»

**No sigue nada.** La línea 26 abre directamente `\subsection{Metodologías de Co-Simulación…}`. La ecuación de índices ($\eta_Q$, $\eta_P$) está en `TEORIA.tex:282`, no aquí. Es un resto de edición: o se elimina la frase o se trae la ecuación.

---

## M-14 a M-17 · Menores

**M-14 · $K_{i,\text{pll}}$ redondeado a la baja.** $K_i = \omega_n^2 = (2\pi\cdot7.5)^2 = 2220.66$. El documento publica 2220.0 en `TEORIA.tex:47` y `IMPLEMENTACION.tex:79`. Diferencia de 0.66 (0.03 %) — sin efecto práctico, pero es el tipo de cifra que un jurado recalcula.

**M-15 · Los 6.8 kvar no se derivan.** `IMPLEMENTACION.tex:105` justifica las cinco potencias base (3.0 + 4.5 + 5.0 + 2.5 + 2.0 = 17.0 kW ✓) pero presenta 6.8 kvar sin ecuación. Implica $Q/P = 0.40$, es decir un factor de potencia de **0.928**, que el texto no declara. Si es un supuesto de diseño, hay que escribirlo.

**M-16 · El tiempo de asentamiento del PLL no declara su banda.** `TEORIA.tex:53` usa $t_s \approx 4.75/\omega_n \approx 100$ ms. Para $\zeta = 1$ la respuesta es $(1+\omega_n t)e^{-\omega_n t}$; el coeficiente 4.75 corresponde a la banda del **5 %** (2 % daría 5.83 → 123.8 ms; 1 % daría 6.64 → 140.9 ms). Como el documento adopta $\varepsilon = 2\%$ en otro sitio, la banda debe declararse explícitamente.

### Corrección aplicada

**M-14.** $\omega_n = 2\pi \cdot 7{,}5 = 47{,}1239$, no $47{,}12$. Se sustituyó en `TEORIA.tex:46-47` y el integrador pasó a $2220.66$ en las **tres** apariciones: `TEORIA.tex:47`, `IMPLEMENTACION.tex:79` y `DISENO.tex:11`. Verificado: $2(47{,}1239) = 94{,}2478 \approx 94{,}25$ ✓ y $(47{,}1239)^2 = 2220{,}66$ ✓. El `2220.0` de `DISENO.tex:11` fue un hallazgo residual de la propia revisión: quedaba fuera del alcance declarado y se corrigió en una segunda pasada.

**M-15.** Se añadió la derivación en `IMPLEMENTACION.tex:105`: «…lo que corresponde a una relación $Q/P = 0.40$ y a un factor de potencia agregado de $0.928$, adoptado de forma uniforme en los cinco nodos». $6{,}8/17{,}0 = 0{,}40$ exacto; $\cos(\arctan 0{,}4) = 0{,}928$.

**M-16.** Se declaró la banda en `TEORIA.tex:53` —«criterio de banda del $5\,\%$; con banda del $2\,\%$ serían $124\text{ ms}$»— y en forma corta en `DISENO.tex:11`. Para $\zeta = 1$ la respuesta es $(1+\omega_n t)e^{-\omega_n t}$: la banda del 5 % da $\omega_n t = 4{,}74$ y la del 2 % $5{,}83/\omega_n = 123{,}7$ ms.

**M-17.** `PROBLEMA.tex:19` *ignora* · `JUSTIFICACION.tex:18` *los sistemas* · `INTRODUCCION.tex:6` *agrava* (una relación $R/X \ge 1$ no «ayuda» a que aparezcan desviaciones: las agrava).

**Verificado en el PDF compilado:** $2220{,}66$ tres veces y $2220{,}0$ cero; $0{,}928$; $124\text{ ms}$; «los sistemas SCADA»; «agrava»; «ignora las dinámicas». Sin regresiones: $3{,}981$, $0{,}251$, $g_{\text{ef}} = 1{,}033$, CFL $1{,}677$, $-18{,}1$ dB y $52{,}54$ s intactos.

---

**M-17 · Concordancia.**
- `PROBLEMA.tex:19`: «Esta desconexión metodológica (…) **ignoran** las dinámicas» → *ignora* (sujeto singular).
- `JUSTIFICACION.tex:18`: «infraestructuras (…) como **el sistemas** SCADA» → *los sistemas*.
- `INTRODUCCION.tex:6`: «lo cual **ayuda a** la aparición de desviaciones nodales» → el alta relación $R/X$ no *ayuda* a que aparezcan: las *agrava* o *induce*. Verbo invertido por descuido.

---

## Lo que verifiqué y está correcto

Para que el informe no se lea como si todo estuviera mal:

| Elemento | Verificación |
|---|---|
| Cota de Lyapunov (`eq:t_settling`) | Derivada y reproducida: $T_1 = 21.4355$ s, $T_2 = 31.1011$ s, **suma 52.5366 s** ✓ |
| Consistencia cota ↔ derivada | $1/(a(1-p))$ reproduce exactamente $T_1$ ✓ |
| $\lambda_2 = 2(1-\cos\pi/3) = 1.0$ | ✓ idéntico al valor del código |
| Ganancias del PLL | $K_p = 94.2478$ (publicado 94.25 ✓), $\omega_n = 47.1239$ ✓ |
| $\rho = H/h = 500$, $N_{substeps} = 500$ | ✓ |
| $4$ ciclos $\times$ 0.5 s = 2.0 s | ✓ |
| $\pm\pi$ rad/s = $\pm0.5$ Hz | ✓ |
| Potencias base suman 17.0 kW | ✓ |
| Ecuación de oscilación, droop, Clarke-Park, $dq$, PLL, PV, BESS, eólico, hidráulico, flujo de potencia | Correctas y con la forma estándar de la literatura citada ✓ |
| Distinción de las tres bandas de frecuencia | Correctamente expuesta en `IMPLEMENTACION.tex:125` ✓ |
| Referencias | 47 citadas, 0 sin entrada, 0 duplicados, todas resueltas ✓ |
| Estructura LaTeX | 0 refs rotas, 0 labels duplicados, entornos balanceados ✓ |
| Métricas del diseño definidas en teoría | RMSE, nadir, RoCoF, $T_{set}$, $\tau_{crit}$ — todas ✓ |

**48 ecuaciones etiquetadas; 30 no se referencian después.** No es un error, pero una tesis con 30 ecuaciones presentadas y nunca citadas sugiere apéndice o reducción.

---

## Prioridad de corrección

| Orden | Hallazgo | Coste | Efecto |
|---|---|---|---|
| 1 | **M-01** (c1/c2 en implementación) | 1 línea | Elimina la contradicción más visible |
| 2 | **M-02/M-03** (régimen de exponentes) | 1 frase | Corrige física invertida |
| 3 | **M-06** (seis → siete secciones) | 2 líneas | Cierra el desajuste de estructura |
| 4 | **M-04** (−24 → −18.1 dB) | 1 cifra | Elimina una afirmación falsa |
| 5 | **M-07** (seguidores) | 1 acotación | Alinea alcance con validación |
| 6 | **M-13** (frase huérfana) | borrar 2 líneas | Limpieza |
| 7 | M-05, M-09, M-11 | párrafos | Requieren decisión de fondo |
| 8 | ~~M-12, M-14–M-17~~ | — | Cerrados el 2026-11-04 |

**Cerrado el 2026-11-04:** M-08a (la cifra de $T_{set}$ se calculaba con $\varepsilon = 0.5\%$ mientras la ecuación define $\varepsilon = 0.02$; corregida a 13.5 s / 26 %), M-08b (la zona muerta pasó de `\epsilon` a `\delta`, para no confundirse con la banda) y M-10 (la pendiente de empalme se publica ahora para ambos exponentes, 3.981 y 0.251, y la `\gamma` indefinida se sustituyó por `p`). M-08c se descartó: `\varepsilon_{\text{ZOH}}` está subindexado y se distingue solo.

Los tres primeros son los que un jurado encuentra en los primeros diez minutos.
