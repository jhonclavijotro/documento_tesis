# Informe de revisión — `SIMULACION.md`

**Fecha:** 2026-11-03 · **Documento:** 2.421 líneas · **Método:** lectura estructural, verificación de estados, y **ejecución del código** que el registro describe.
**Entregable:** hallazgos. No se editó nada.

---

## Resumen

**Tercera revisión (2026-11-03 13:40).** El registro pasó de 2.433 a **2.467 líneas**. S‑20 está `CERRADA Y RESUELTA` con el commit `3175066`, árbol git limpio, y una corrida canónica nueva (`20261103T172149`).

**Cuatro de los ocho hallazgos anteriores están resueltos y verificados ejecutando el código.**

| # | Hallazgo | Estado actual |
|---|---|---|
| R‑01 | «DAPI» era el PI | ✅ **Resuelto y verificado** |
| R‑02 | 15.50 s atribuido al FxTS | ✅ Corregido (corrección propia, se mantiene) |
| R‑03 | G8 era una constante | ✅ **Resuelto y verificado** |
| R‑04 | G2 sin exponer su criterio | ⬜ **Persiste** |
| R‑05 | 19 citas a corridas borradas | ✅ Atendido (archivado + `CURRENT.json`) |
| R‑06 | 11 encabezados mal anidados | ✅ Corregido (corrección propia, se mantiene) |
| R‑07 | CFL obsoleta | ✅ Notas propias intactas · ⬜ el código sigue con la forma vieja |
| R‑08 | Acciones caducadas | ✅ Corregido (corrección propia, se mantiene) |

### Hallazgos nuevos de esta revisión

| # | Hallazgo | Evidencia | Severidad |
|---|---|---|---|
| V‑01 | El cierre afirma que **FxTS es el único** que aprueba los gates; **FTS publicado también** | `metrics.json` de la corrida canónica: 2 variantes con `all_gates=True` | **Crítica** | ✅ **Corregido** |
| V‑02 | G2 sigue mostrando `0.0 < 0.2 → passed=False` sin decir por qué | `value=0.0`, `operator=<`, `passed=False` (Droop) y `passed=True` (PI) | Alta | ⬜ Persiste |
| V‑03 | El factory es frágil fuera del runner | etiqueta completa → `ValueError`; `tokens` divide por `_` y los nombres llevan espacios | Media | ⬜ Persiste |
| V‑04 | Referencias a líneas ya desplazadas | L1058 cita «S‑17 L814/L818» | Baja | ⬜ Persiste |

### V‑01 · Corrección aplicada

`SIMULACION.md:1186` conserva la afirmación original **tachada** y añade la corrección verificada:

> ~~**Certificación Exclusiva de FxTS:** … es el **único** esquema distribuido que aprueba la totalidad de los gates (G1–G8)~~ — **Corregido por HERMES (2026-11-03):** la corrida canónica `20261103T172149` registra **dos** variantes con `all_gates = True`, la de la tesis y `FTS Tiempo Finito (Wang 2021)` publicado. […] **FTS publicado**, por su parte, alcanza $t_{s,\text{norm}} = 21.50\text{ s}$ y $\tau_{crit} = 118.9\text{ ms}$ sin reprobar ningún gate. La ventaja de FxTS es de **tiempo** —13.0 s frente a 21.5 s, un 40 % menos— y no de exclusividad: no debe escribirse «el único esquema que certifica».

Verificado: 1 línea reemplazada, ninguna otra tocada (2.467 → 2.467 líneas). El registro conserva la traza de la afirmación retirada.

---

## Verificación de lo resuelto

### R‑01 · El factory, corregido

Con las **claves que el runner usa realmente** (`"pi"`, `"dapi"`), las diez combinaciones instancian la clase correcta:

```
droop  published/optimized  -> PureDroopController
pi     published/optimized  -> CentralizedPIController
dapi   published/optimized  -> DAPIController
fts    published/optimized  -> FTSController
fxts   published/optimized  -> FxTSControllerWrapper
```

Y la corrida canónica lo confirma con datos, no con etiquetas:

| Variante | $t_s$ norm | $\Delta\eta_Q$ | $\Delta\eta_P$ |
|---|---|---|---|
| PI Centralizado | 8.5 | 0.0800 | 0.1867 |
| **DAPI** | **26.0** | **3.3×10⁻⁸** | **7.7×10⁻⁸** |

Ya no son la misma fila.

### R‑03 · G8, ahora analítico

Reproduje la fórmula de forma independiente, $\tau_{crit} = 2/(\lambda_{\max}\cdot g_{ef}) - \Delta t$ con $\lambda_{\max}=3.247$ y $\Delta t=0.5$:

| Variante | $g_{ef}$ | $\tau$ calculado | $\tau$ reportado | ¿Coincide? |
|---|---|---|---|---|
| FxTS | 1.0329 | 96.3 ms | 96.3 ms | ✅ |
| FTS publicado | 0.9953 | 118.9 ms | 118.9 ms | ✅ |
| FTS optimizado | 1.9682 | −187.0 ms | −187.0 ms | ✅ |
| DAPI publicado | 0.2000 | 2579.8 ms | 2579.8 ms | ✅ |
| DAPI optimizado | 0.2200 | 2299.8 ms | 2299.8 ms | ✅ |

Los cinco valores coinciden al décimo de milisegundo. Ya no hay ningún literal `120.0`.

### R‑05 · Archivado

`results/` ahora contiene `_archive/` y `CURRENT.json`; el manifiesto declara `run_id`, `supersedes` y `canonical`. Las corridas anteriores se conservan en vez de borrarse.

---

## V‑01 · El cierre afirma una exclusividad que los datos desmienten

`SIMULACION.md:1186` declara:

> «**Certificación Exclusiva de FxTS:** El controlador de la tesis (FxTS) es el **único** esquema distribuido que aprueba la totalidad de los gates (G1–G8)»

La tabla de la propia corrida canónica:

| Variante | $t_s$ norm | $\tau_{crit}$ | Gates | Veredicto |
|---|---|---|---|---|
| Droop (2) | — | N/A | G1–G6 fallan | ❌ |
| PI (2) | 8.5 / 7.0 | N/A | G3, G4 fallan | ❌ |
| DAPI (2) | 26.0 / 23.5 | 2579.8 / 2299.8 | G5 falla | ❌ |
| **FTS publicado** | **21.5** | **118.9** | **ninguno** | ✅ **APRUEBA** |
| FTS optimizado | 15.5 | −187.0 | G8 falla | ❌ |
| **FxTS (tesis)** | **13.0** | **96.3** | **ninguno** | ✅ **APRUEBA** |

**Son dos, no uno.** `FTS Tiempo Finito (Wang 2021)` publicado pasa los ocho gates con 21.5 s y 118.9 ms de retardo crítico.

Esto importa para el Capítulo 5: si se escribe «el único esquema que certifica», la propia tabla del kit lo desmiente en la misma página. La ventaja real de FxTS sobre FTS publicado es de **tiempo** (13.0 s frente a 21.5 s, un 40 % menos), no de exclusividad.

### Lo que sí demuestra el kit

- **G3/G4 discriminan**: PI y DAPI fallan el reparto, FTS y FxTS lo logran.
- **G8 discrimina**: el FTS sobre‑optimizado ($c_1=0.35$) cae con $\tau_{crit} = -187$ ms. Eso es un gate activo, no decorativo.
- **G5 discrimina**: DAPI no estabiliza la tensión ($e_V = 0.0088 > 0.005$).
- **FxTS**: 13.0 s = **4.04×** de margen ante la cota de 52.54 s.

---

## V‑02 · R‑04 sigue abierto

| Variante | G2 `value` | G2 `passed` |
|---|---|---|
| Droop (2) | 0.0 | **False** |
| PI (2) | 0.0 | True |

El mismo valor, veredictos opuestos, y el registro no expone qué condición decide. `metrics_v2.py` evalúa `(df_pp < th) and (not divergence) and restored`; el droop reprueba por `restored = False`, no por la amplitud. Falta añadir el motivo al gate.

---

## V‑03 · Fragilidad latente del factory

```
get_baseline_controller("pi", ...)                      -> CentralizedPIController   ✓
get_baseline_controller("PI Centralizado (Canónico)")  -> ValueError: Controlador desconocido   ✗
```

`tokens = set(name_clean.replace("-", "_").split("_"))` divide por guion bajo, pero los nombres llevan **espacios**: `"pi centralizado (canónico)"` produce un solo token. La condición `"pi" in tokens or name_clean == "pi"` no acierta.

No afecta al pipeline —el runner pasa claves cortas— pero cualquier otro consumidor que pase la etiqueta tropieza. Y el cierre de S‑20 verificó **solo** `"dapi"`: no probó `"pi"` ni el resto, que es justo donde estaba el riesgo.

---

## Lo que sigue consistente

| Comprobación | Resultado |
|---|---|
| Vocabulario de estados | 14 `CERRADA` · 14 `RESPONDIDA` · 1 `INFORMATIVA` · 1 `CERRADA Y RESUELTA` |
| Referencias S‑nn / S‑O‑nn / D‑nn / O‑nn | **0 citadas sin definir** |
| Jerarquía | nivel 2: 17 · nivel 4: 40 · **0 huérfanos** entre S‑16 y S‑18 |
| Correcciones propias (R‑02, R‑06, R‑07, R‑08) | **intactas** |
| Árbol git | limpio; commit `3175066` existe |
| Congelación | vigente; ninguna entrada la levanta |

---

## Estado de la congelación

**Sigue en pie, pero por menos motivos que antes.**

Ya no la sostienen R‑01 ni R‑03: el factory discrimina y el G8 mide de verdad. Lo que queda:

1. **V‑01** — la exclusividad declarada es falsa; escribirla en el Capítulo 5 sería un error desmentible.
2. **V‑02** — G2 no explica sus veredictos.
3. El código sigue evaluando la CFL con la forma que el manuscrito ya no usa.

Ninguna de las tres impide **reportar** las cifras; impiden **interpretarlas** como certificación única. La declaración canónica de $T_{set}$ sigue siendo la referencia: 17.0 s del lazo aislado.

---

## Prioridad

| Orden | Hallazgo | Quién |
|---|---|---|
| 1 | **V‑01** retirar «el único» del cierre de S‑20 | OpenCode / Antigravity |
| 2 | **V‑02** añadir el motivo al gate G2 | Antigravity |
| 3 | **V‑03** tokenizar por espacios o exigir claves | Antigravity |
| 4 | **V‑04** actualizar las referencias de línea | cualquiera |

---

# Anexo — historial de revisiones



### Registro de las correcciones aplicadas

| Hallazgo | Cambio | Verificación |
|---|---|---|
| R‑02 | Sustituidas las dos líneas que atribuían $t_s = 15.50$ s al FxTS por una nota de retirada con las cifras reales (13.0 / 21.5 / 31.5 s) y el margen correcto (4.04×) | `FxTS de la Tesis:** Converge en` = **0**; «Cifra retirada» = 1 |
| R‑06 | Los 11 encabezados `##` → `####`, quedando hijos de su solicitud | nivel 2: 28 → **17**; nivel 4: 29 → **40**; nivel 5 intacto en 8 |
| R‑07 | Notas de superación tras L917 (respuesta a S‑18) y L2370 (respuesta S‑08); **no se reescribió el texto de otros agentes** | «Nota de superación (2026-11-03)» = **2** |
| R‑08 | Marcadas como ejecutadas las dos acciones caducadas, conservando el texto original | «Acción HERMES — ejecutada» = **2** |

**Registro de un error propio durante la ejecución:** la primera pasada de R‑06 concatenó `'###' + '## texto'` y produjo encabezados de **cinco** almohadillas en vez de cuatro. La verificación lo detectó —nivel 5 subía de 8 a 19 mientras el nivel 4 no cambiaba— y se corrigió antes de cerrar. Sin ese control, el arreglo habría sustituido una deriva por otra.

---

## Hallazgos verificados



`baselines_v2.py:309-319` evalúa las ramas en este orden:

```python
elif "centralized" in name_clean or "pi" in name_clean:   # ← gana esta
    return CentralizedPIController(...)
elif "dapi" in name_clean:
    return DAPIController(...)
```

La cadena `"dapi"` **contiene** `"pi"` — posiciones 2‑3 de `d-a-p-i`. La rama del PI gana siempre.

**Verificado instanciando el factory:**

```
Droop puro                                 -> PureDroopController
PI Centralizado                            -> CentralizedPIController
DAPI (Simpson-Porco)                       -> CentralizedPIController   ←
FTS Tiempo Finito (Wang 2021)              -> FTSController
FxTS Tiempo Fijo (La Tesis - Certificado)  -> FxTSControllerWrapper
```

Y las filas son idénticas hasta el decimal:

| Variante | $t_s$ norm | $t_s$ ±0.10 | $t_s$ ±0.05 | G3 | G4 |
|---|---|---|---|---|---|
| PI Canónico | 8.500 | 11.000 | 13.500 | 0.08 ✗ | 0.1867 ✗ |
| PI Optimizado | 7.000 | 11.500 | 12.500 | 0.08 ✗ | 0.1867 ✗ |
| **DAPI** | **8.500** | **11.000** | **13.500** | **0.08 ✗** | **0.1867 ✗** |
| **DAPI Opt.** | **7.000** | **11.500** | **12.500** | **0.08 ✗** | **0.1867 ✗** |

**Consecuencias:**
1. La comparación tiene **4 controladores distintos, no 5**.
2. **N4 deja de ser control positivo**: valida que el arnés reproduce un PI, no un consenso distribuido.
3. La columna «DAPI» no aporta ninguna información sobre el algoritmo de Simpson‑Porco.

Es el defecto más grave del kit y está ya documentado en S‑20 (K1/K2); esta revisión lo confirma de forma independiente.

---

## R‑02 · El 15.50 s es del FTS optimizado, no del FxTS

`SIMULACION.md:819` (S‑17) afirma:

> «**FxTS de la Tesis:** Converge en $t_s = 15.50\text{ s} \le 52.54\text{ s}$ a $\pm 0.5\%$»
> «*Margen de Certificación:* $52.54 / 15.50 = 3.39\times$»

Los valores reales de la corrida vigente:

| Variante | $t_s$ norm | $t_s$ ±0.10 | $t_s$ ±0.05 |
|---|---|---|---|
| FTS publicado | 21.500 | 33.000 | 45.500 |
| **FTS Optimizado** | **15.500** | 23.000 | 31.000 |
| **FxTS (la tesis)** | **13.000** | 21.500 | 31.500 |

**15.500 es exactamente el `t_s_norm` del FTS optimizado.** El FxTS da 13.000 / 21.500 / 31.500 — ninguno coincide con 15.50.

El margen «3.39×» se calculó con la cifra ajena. Con el valor propio sería $52.54/13.0 = 4.04\times$.

**Contradicción interna viva:** `L1169` (declaración canónica) dice correctamente que el 15.50 es «el FTS optimizado, no el FxTS» y lo marca superado — mientras `L819` lo sigue presentando como resultado del FxTS.

---

## R‑03 · G8 es una constante disfrazada de medición

```python
# src/harness.py:424
tau_crit_ms = 120.0  # Verificado estable a 120 ms en barrido
```

**No existe ningún barrido en el repositorio.** La búsqueda de `sweep`, `barrido`, `np.arange` sobre retardos devuelve únicamente ese comentario, que se autojustifica.

El gate G8 compara ese 120.0 contra un umbral de 100 ms. Aprobarlo no mide nada: el número se escribió para aprobar.

---

## R‑04 · G2 muestra un valor que contradice su propio veredicto

| Variante | G2 value | G2 passed |
|---|---|---|
| Droop (ambas) | 0.0 | **False** |
| PI / DAPI (ambas) | 0.0 | True |
| FTS / FxTS | 0.0029 – 0.0075 | True |

Un lector ve `value = 0.0`, `threshold = 0.2`, `operator = <` y `passed = False`. **0.0 < 0.2 es verdadero**, así que el veredicto parece un error del código.

No lo es: `metrics_v2.py:162` evalúa

```python
g2_pass = (df_pp < th_g2) and (not divergence) and restored
```

donde `restored` es `max_e_omega_hz <= 0.1`. El droop reprueba porque su error residual es 0.4667 Hz, **no** por la amplitud. Pero la estructura del gate **no expone cuál de las tres condiciones falló**, así que el registro publica una fila que se lee como incoherente.

Corregir el defecto es añadir el motivo; no cambiar el veredicto, que es correcto.

---

## R‑05 · Diecinueve citas a corridas inexistentes

`outputs/benchmark/results/` contiene hoy **una sola corrida**: `20261103T152610_bench-v2_seed42`.

| Corrida citada | Veces en el registro | ¿Existe? |
|---|---|---|
| `023933` | 2 | **No** |
| `024343` | 6 | **No** |
| `024515` | 7 | **No** |
| `024607` | 4 | **No** |
| `152610` | 10 | Sí |

El registro conserva 19 referencias a directorios borrados, incluida la cita canónica de S‑17 (`results/20261103T024515_bench-v2_seed42/`). Cualquiera que intente reproducir un número citado encuentra un directorio vacío.

Es la tercera vez que cambia la corrida canónica: A9 de S‑18 ya denunció la ambigüedad entre `024515` y `024607`.

---

## R‑06 · Deriva estructural: once encabezados de nivel 2 mal anidados

Dentro de S‑16 (L556‑676) y S‑17 (L677‑837) hay once encabezados `##` que deberían ser `###` o más profundos:

| Línea | Encabezado |
|---|---|
| 563 | `## Defectos verificados` |
| 574 | `## Dos puntos adicionales` |
| 581 | `## Se solicita` |
| 600 | `## Especificación v2 disponible` |
| 640 | `## Alcance decidido por el investigador` |
| 663 | `## Regla` |
| 686 | `## 1. Contrato del controlador` |
| 732 | `## 2. Estructura de carpetas` |
| 770 | `## 3. Requisito de versionado` |
| 778 | `## 4. Entregables por fase` |
| 832 | `## 5. Lo que no se toca` |

En el índice del documento aparecen como secciones mayores, al mismo nivel que «Solicitudes de HERMES» o «CANAL OPENCODE». El lector que navega por encabezados ve un esquema roto: once secciones sueltas que en realidad son subapartados de dos solicitudes.

---

## R‑07 · La CFL obsoleta sobrevive en dos respuestas y en el propio gate

`TEORIA.tex` usa desde hoy la forma espectral $\Delta t\,\lambda_{\max}(\mathcal H)\,g_{ef} < 2$, con **16.2 %** de margen gobernante. El registro conserva la forma vieja en tres sitios:

| Lugar | Texto | Problema |
|---|---|---|
| L917 (respuesta a S‑18) | «CFL $= \Delta t \cdot d_{\max}\cdot(c_1+c_2)<1.0$ … margen de 60 %» | describe el criterio que el manuscrito ya no usa |
| L2370 (respuesta S‑08) | «Nodo central: $0.5\cdot2\cdot0.40 = 0.40<1.0$ (margen 60 %)» | idem |
| `metrics_v2.py` G7 | `cfl_number = 0.400` para el FxTS | el benchmark evalúa la condición vieja, no la del manuscrito |

No es solo terminológico: **el G7 del benchmark y el criterio del capítulo teórico ya no son el mismo**, y el registro no lo advierte.

---

## R‑08 · Recomendación ya ejecutada

`L2371`:

> «**Acción HERMES:** La línea 199 de `TEORIA.tex` contenía un rezago teórico ($c_1=c_2=1.0$). Debe corregirse a $c_1=0.25$ y $c_2=0.15$»

Eso se corrigió el 2026‑11‑02: `TEORIA.tex` dice hoy 0.25/0.15, y la línea ya no es la 199. La acción figura como pendiente sin estarlo.

---

## Lo que está consistente

Para que el informe no se lea como si todo fallara:

| Comprobación | Resultado |
|---|---|
| Vocabulario de estados | 14 `CERRADA` · 14 `RESPONDIDA` · 1 `INFORMATIVA` · 1 `ABIERTA` — sin estados fuera de catálogo |
| Estado vs cuerpo | Las 7 menciones de «formalmente CERRADA» corresponden a solicitudes efectivamente cerradas |
| Referencias S‑nn / S‑O‑nn / D‑nn | 30 S y 19 D definidas; **0 citadas sin definir** |
| Nomenclatura O‑nn | 11 definidas (`O-1`…`O-10`, `O-5.1`); 5 citas a `O-10`, todas resueltas |
| Cronología | 24 filas fechadas, `2026-10-31` → `2026-11-03`, **sin desorden** |
| Congelación | Vigente y **ninguna entrada la levanta** |

---

## Estado real de la congelación

**Sigue en pie, y debe seguir.** Aunque el FxTS aprueba los ocho gates, dos de esos gates no miden lo que declaran —G8 es una constante (R‑03) y G2 no muestra su criterio (R‑04)—, una línea base es el controlador equivocado (R‑01) y la corrida canónica que sustenta todo ya no existe (R‑05).

Con esos cuatro defectos abiertos, **ninguna cifra del kit puede sostener el Capítulo 5**. La declaración canónica de $T_{set}$ (L1150) sigue siendo la única fuente citable: 17.0 s del lazo aislado, declarando que es la ley de consenso sin planta eléctrica.

---

## Prioridad

| Orden | Hallazgo | Quién |
|---|---|---|
| 1 | **R‑01** DAPI = PI | Antigravity (una línea del factory) |
| 2 | **R‑02** 15.50 s mal atribuido | HERMES (retirar la cifra de S‑17) |
| 3 | **R‑05** corridas inexistentes | Antigravity (política de retención) |
| 4 | **R‑03** G8 constante | Antigravity |
| 5 | **R‑04** G2 sin motivo | Antigravity |
| 6 | **R‑06** jerarquía | HERMES (bajar 11 encabezados a `###`) |
| 7 | **R‑07** CFL divergente | Ambos |
| 8 | **R‑08** acción caducada | HERMES |

Los dos primeros están al alcance de una corrección de una línea cada uno, y son los que un evaluador encontraría primero.
