# Informe de revisión global del manuscrito

**Documento:** `D:\TEXTOS\TESIS` — `main.tex` + `SECCIONES/*.tex` + `TuArchivo.bib`
**Fecha:** 2026-11-08
**Alcance:** coherencia global tras el cierre de la sección 8 (Resultados y Discusión).
**Regla aplicada:** cada hallazgo se reporta antes de tocarse y se aplica por etapas aprobadas.

---

## 1. Métricas de partida (2026-11-08)

| Métrica | Al inicio | Al cierre del bloque |
|---|---|---|
| Secciones numeradas | 8 | 8 |
| Citas distintas | 47 · entradas `.bib` 54 | **52 citadas · 52 entradas** |
| Claves citadas sin entrada | 0 | 0 |
| Entradas sin citar | 7 | **0** |
| Métricas del diseño sin definición en teoría | 0 | 0 |
| Duplicados en `.bib` | 0 | 0 |
| Balance de entornos LaTeX | OK en las 10 secciones | OK |
| Compilación | 75 páginas · 741 131 B | **78 páginas · 749 001 B** · 0 errores · 1 overfull |

Scripts ejecutados: `coherencia_tesis.py`, `auditar_referencias.py`, `check_entornos.py`.

---

## 2. Hallazgos

| ID | Hallazgo | Evidencia | Estado |
|---|---|---|---|
| **H1** | La introducción anuncia siete secciones y el documento tiene ocho; falta *Resultados y Discusión* en el listado. | `INTRODUCCION.tex:24` y sus siete `\item` | **CERRADO** (2026-11-08) |
| **H2** | El cuarto objetivo específico exige validar latencia, pérdida de paquetes y desconexión de enlaces; el capítulo lo aplazaba «fuera de este capítulo» sin artefacto ni lugar donde declararlo. | `OBJETIVOS.tex:14`; `DISENO.tex:29,36`; `RESULTADOS.tex:344` | **CERRADO** (2026-11-08) — campaña `20261108T170925_resilience_seed42` verificada desde su telemetría (601 filas; $e_Q$ máx 0.0009 nominal y 0.0000 con falla; $f$ mín 59.9894 Hz; 194/3606 paquetes descartados) e incorporada en la Familia 3 |
| **H3** | Las constantes del soporte local (diésel y BESS) no estaban en el manuscrito y $k_p$ estaba ocupado por la pendiente de la zona muerta. | `distributed_node_runner.py:82,83,246,253`; `TEORIA.tex:209-211` | **CERRADO** (2026-11-08) |
| **H4** | El capítulo nombra ESC-HIL-001 mientras el escenario activo es ESC-HIL-003 y las figuras de contexto provienen de este último. | `RESULTADOS.tex` (3 menciones) | **CERRADO** (2026-11-08) |
| **H5** | El módulo citado se llama `finite_time_consensus.py` en un trabajo que reivindica tiempo fijo (FxTS). | `IMPLEMENTACION.tex:109` | **CERRADO** (2026-11-08) — renombrado a `fixed_time_consensus.py` con shim y corrida `20261108T161211` |
| **H6** | Siete entradas del `.bib` sin citar. | `auditar_referencias.py` | **CERRADO** (2026-11-08) — 52 citadas / 52 entradas |

### Verificaciones que salieron limpias
- Terminología: FTS (base, tiempo finito) y FxTS (propuesta, tiempo fijo) consistentes; la única aparición de «tiempo finito» en RESULTADOS está en la enumeración de los cinco algoritmos.
- Parámetros repetidos: $\alpha=0.8$, $\beta=1.2$, $c_1=0.25$, $c_2=0.15$, $\lambda_2=1.0$, $T_f \le 52.54$ s idénticos en TEORIA, IMPLEMENTACION y RESULTADOS. Los valores $c_1=0.207/c_2=0.193$ y $c_1=0.15/c_2=0.25$ son puntos de sensibilidad declarados.
- Alcance principal: los cuatro estados de consenso del objetivo general coinciden con los lazos implementados.
- Sin referencias numéricas escritas a mano (todo por `\ref`/`\eqref`).

---

## 3. Cambios aplicados

### H1 — introducción a ocho secciones
`INTRODUCCION.tex`: «siete» → «ocho secciones fundamentales» y `\item` nuevo para *Resultados y Discusión*. Ocho `\item`; los siete previos intactos.
**Verificación:** 76 páginas · 741 783 B · 0 errores · 0 indefinidas · 1 overfull.

### H2 — estatuto de la campaña de resiliencia
`RESULTADOS.tex:344`: se retira «cien semillas … fuera de este capítulo» y se declara la campaña en construcción —ESC-HIL-005 y escenario de fallas telemáticas con latencia 50–500 ms, pérdida 0–30 % y desconexión de enlace, conforme a las actividades 3.3 y 4.2—, acotando lo validado: cuatro estados de consenso en T1 y, en el banco, reactiva más frecuencia por el lazo integral del diésel. La tolerancia al fallo telemático queda declarada como pendiente de evidencia.
**Verificación:** 76 páginas · 742 262 B · 0 errores · «cien semillas» y «fuera de este capítulo» = 0 en el PDF.

### H3 — constantes del soporte local y desambiguación de $k_p$
`IMPLEMENTACION.tex`: ecuación nueva `eq:rest_local` con $\kappa_{p,\omega}=250$ W/(rad/s), $\kappa_{i,\omega}=80$ W/rad, anti-windup $\pm 75$ rad ≡ $\pm 6.0$ kW sobre base de 4.0 kW ($10.0$ kW de eje ≡ $9.5$ kW eléctricos) y $\kappa_{\text{BESS}}=40$ W/(rad/s) sobre 0.75 kW, cada uno con su criterio.
`RESULTADOS.tex`: $k_p \to \kappa_{p,\omega}$ en la Fase III y remisión a `\eqref{eq:rest_local}` en la Fase V; cifras de `eq:res_droop_backup` intactas. `TEORIA.tex` sin tocar.
**Verificación:** 76 páginas · 743 885 B · 0 errores · `k_p` = 0 en RESULTADOS · ecuación (46) resuelta.

### H6 — bibliografía cerrada sin residuos
Se citaron cinco entradas que respaldaban afirmaciones ya presentes y se depuraron las que no pertenecían al alcance. Antes de citar se resolvió cada DOI contra CrossRef: `Li2019` (`10.1080/21642583.2019.1695689`) y `Salman2024` (`10.1109/ACCESS.2024.3414603`) existen y coinciden en título, autor, revista y año; `Glover2017` es el libro de Cengage con ISBN 9781305632134; `Gupta2026` es una nota de prensa de SolarQuarter cuya URL responde HTTP 200.
`Arpana2025` resultó **DUDOSA** —sin DOI, sin revista y sin registro en CrossRef ni en OpenAlex— y se sustituyó por una referencia verificable sobre el mismo tema: `Mehmood2021`, *Edge Computing for IoT-Enabled Smart Grid*, Security and Communication Networks, vol. 2021, pp. 1–16, DOI `10.1155/2021/5524025`. Se eliminaron `Shah2026` y `Ozturk2024` por quedar fuera del alcance.
Ubicación de las citas: `Gupta2026` en el primer párrafo de INTRODUCCIÓN; `Li2019` en la enumeración de familias de consenso y `Salman2024` en el párrafo de consenso óptimo de ANTECEDENTES; `Mehmood2021` en la oración sobre *Edge Computing* e *IoT*; `Glover2017` en el ítem del algoritmo FBS de TEORÍA.
**Verificación (recompilación limpia con `latexmk -C` + `bibtex`):** 77 páginas · 746 051 B · 0 errores · 0 referencias indefinidas · 1 overfull · **0 warnings de bibtex** · **52 claves citadas para 52 entradas**, sin citadas-hacia-fuera ni entradas sin citar. Respaldo del `.bib` original en `TuArchivo.bib.bak_20261108`.

### H4 — procedencia del escenario
`RESULTADOS.tex` (apartado de plataforma): declara que el ensayo se ejecutó sobre ESC-HIL-001 y que su versión consolidada ESC-HIL-003\_consolidado\_rev5 es numéricamente equivalente (delta máximo nulo en dieciocho series × 601 muestras), y atribuye las series de las Figuras 4 y 5 a los archivos consolidados.
**Verificación:** 76 páginas · 744 469 B · 0 errores · tres menciones a ESC-HIL-001 coherentes entre sí · `\ref` a las figuras 4 y 5 resueltos.

---

## 4. Marco de evaluación del control secundario (D-24, decisión del investigador)

La validación del lazo secundario MAS se organiza en **tres familias de escenario**; cada una exige su escenario y su criterio. El capítulo se reestructuró para reflejarlo: el ensayo de déficit conserva sus cinco fases y el resto de familias se declaran con escenario y criterio, sin cifras hasta que existan las corridas.

| Familia | Condición | Evidencia | Estado |
|---|---|---|---|
| **1 · Déficit de capacidad** | la generación disponible no alcanza; la frecuencia se degrada | ESC-HIL-001: 12.594 kW sobre 11.535 kW firme · 59.0414 ± 0.0076 Hz · mínimo 59.0247 Hz · transición monótona · NTC 1340 | **Validado** |
| **2 · Excedente de generación** | la demanda nunca supera la generación, pero la generación sí la supera; el exceso se absorbe o se recorta | ninguna | **No representable**: los tres nodos saturan la consigna en cero (`distributed_node_runner.py:249,255,257`) y el PV no admite techo de inyección. Solicitudes S-36 (capacidad) y S-O-15 (escenario) |
| **3 · Fallas de comunicación** | latencia, pérdida de paquetes y desconexión de enlace entre agentes | ninguna | **En construcción**: S-34 (proxy de inyección y corrida) y S-O-14 (escenario con perfil de falla declarado) |

Consecuencia metodológica que el capítulo ahora declara: en la familia 2 el objetivo de control **cambia de signo** —el consenso reparte una absorción o un recorte, no un déficit—, por lo que el índice de utilización y la cota de saturación son propios y no reutilizan los del reparto reactivo. En la familia 3 lo que se mide es la reconvergencia del lazo bajo red degradada, con la política de último estado conocido como respaldo.

---

## 5. Revisión del registro técnico (2026-11-08)

Ejecutada con `mapa_registro.py` y verificación independiente contra disco, git y los artefactos.

| ID | Hallazgo | Severidad | Estado |
|---|---|---|---|
| **R1** | Árbol de trabajo sucio con trabajo de S-36 sin commitear en el mismo archivo del controlador (+79 líneas: `delta_eta`, `eta_i`, `return_excess`); el hash en disco (`e325258d…`) difiere del certificado (`7ffafca9…`), que corresponde al commit `2eac404` | media | **abierto** — depende de que Antigravity consolide el trabajo de S-36 |
| **R2** | `SECCIONES/RESULTADOS.tex` editado por OPENCODE (retiro de «actualmente en construcción» y alineación de la cadena canónica), fuera del canal exclusivo de HERMES | alta (gobernanza) | **declarado** — el resultado verificado es correcto; queda la regla de canal |
| **R3** | Fila «Puntero canónico» de Evidencias citables desactualizada (`49ab6b2c…`, 2026-11-07) | baja | **corregido** → `1cdac402…`, 2026-11-08 |
| **R4** | El Estado vigente afirmaba que el manifiesto certifica «el código vigente en disco» | baja | **corregido** → certifica el código del commit `2eac404`, con la diferencia del árbol declarada |
| **R11** | Dos cifras de compilación distintas en O-9 (749 001 B y 749 202 B) | baja | **corregido** — la fila de 10:08 queda marcada como superada por la de 10:33 |
| **R12** | El registro decía que `P_discharge_max` del BESS escala «hasta 0.40, nominal sobre 0.40»; el código (`BESS/SistemaBESS.py:94-111`) escala **0.20 → 0.90** | media | **corregido** (2026-11-08) |
| **R13** | El manuscrito cita `152458` / `65feef54…` mientras el registro publica `161211` / `115a6eb9…` | baja | **cerrado** — S-O-17 ejecutada: `:26` cita `161211`/`115a6eb9…`, PDF de 79 páginas verificado |
| **R14** | S-O-14 pide un bloque declarativo `contingencias_telematicas` que D-25 v1 descartó expresamente en favor del séptimo archivo `contingencias_telematicas.csv` | media | abierto — falta el adendo de alineación |
| **R15** | El cierre de S-O-16 afirmaba unicidad canónica; en disco hay **tres** manifiestos con `canonical: true` (vigente + `163357` y `161041` archivados) | media | **corregido** — el bloque declara los tres y fija la regla: la autoridad es `CURRENT.json`; `canonical: true` en `_archive/` no indica vigencia |
| **R16** | El manifiesto no registra el commit de su corrida y los escenarios `ESC-HIL-006/007` están sin versionar | baja | abierto |
| **R17** | Las tres figuras conceptuales (`fig_estructura`, `fig_flujo_datos`, `fig_validacion`) y `FIGURAS.md` no figuran en el registro técnico | media | abierto — falta la entrada informativa con script y hashes |
| **R18** | La Familia 3 del capítulo se declaraba «en construcción» con la campaña de resiliencia ya ejecutada | alta | **corregido** (2026-11-08) — resultados incorporados y verificados; cierra H2 |
| **R19** | El capítulo describía el escenario excedente como «en emisión» estando ya emitido e instalado | baja | **corregido** (2026-11-08) — S-O-20 ejecutada, PDF de 79 páginas verificado |
| **R20** | El `contingencias_telematicas.csv` de la campaña deja `semilla` vacía y no cumple R-L.1 de D-25 | media | abierto — solicitud S-O-19 a Antigravity |

**Verificaciones que sostienen la cadena canónica vigente (`20261108T161211`):** `CURRENT.json` (`6e9932af…`) apunta a esa corrida con `manifest_sha256 = 115a6eb9…`, coincidente con el archivo en disco; `supersedes: 20261108T152458` (archivada intacta); `canonical: true`. Los **ocho hashes del manifiesto coinciden con disco** y el del controlador (`e325258d…`) coincide además con **HEAD** (`d85db09`, S-36 commiteado) y con el árbol limpio: la corrida certifica un commit reproducible. `telemetry.csv` (`24c83332…`), `metrics.json` (`9f10119c…`) y `gates.md` (`9a90ec8a…`) conservan los hashes de las tres corridas anteriores, de modo que el delta cero es verificable. Única omisión: el registro no publica los hashes de `baselines_v2` (`1de02a79…`) ni de `config_bench_8nodos` (`c43361fc…`), que sí están en el manifiesto.

---

## 6. Pendiente

- **H5**: **cerrado**. Antigravity renombró el módulo (`fixed_time_consensus.py` `7ffafca9…` + shim `56c96ac4…`), la suite pasó a 101 pruebas y publicó la corrida `20261108T152458_bench-v2_seed42` (`65feef54…`) con delta cero. El capítulo ya cita el `run_id` y el prefijo nuevos, con la cadena de supersedes (`152458` → `161041` → `163357`).
- **Familia 2 (excedente)**: cerrar S-36 —absorción del BESS con SOC, techo de inyección del PV y reparto del exceso con índice propio— y S-O-15 —escenario con ventana de excedente declarada—. Con esas corridas se completan las dos subsecciones nuevas del capítulo.
- **Familia 3 (fallas de comunicación)**: cerrar S-34 —proxy de inyección sobre ZeroMQ y corrida con telemetría del perfil de falla por paso— y S-O-14 —escenario con bloque `contingencias_telematicas`—.
- **H2**: la subsección de la familia 3 absorbe el compromiso del cuarto objetivo específico; queda pendiente de esas corridas.
