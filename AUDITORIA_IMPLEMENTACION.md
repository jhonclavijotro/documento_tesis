# Auditoría implementación ↔ código — primera pasada

**Alcance de esta pasada:** las afirmaciones de `IMPLEMENTACION` que **nombran un archivo** y contienen un verbo operativo. Se verificó cada nombre de módulo y cada constante declarada contra el repositorio `D:\Antigravity\Projects\Tesis_Grado`.

**Estado: INCOMPLETA.** Se verificaron 6 de los 8 módulos nombrados. Los dos restantes (`Hidrica`, `Diesel`) requieren abrir los archivos, porque los nombres de clase y de constantes no coinciden con los que cita el manuscrito.

## Verificado y correcto

| Módulo citado en el manuscrito | Comprobación | Resultado |
|---|---|---|
| `Solar/SistemaSolar.py` | existe; instancia `MPPTController` y actualiza la referencia cada 0,5 s | correcto |
| `Demanda/SistemaDemanda.py` y `PerfilDemanda` | la clase `PerfilDemanda` está en `Demanda/PerfilDemanda.py`, no en `SistemaDemanda.py` | **nombre de archivo a corregir** |
| `Eolica/SistemaEolico.py` | existe; calcula `Cp(lambda)` y publica `lambda` en el contexto | correcto |
| `common/Transformadas.py` | existe; define la firma `step(dt, V_pcc, setpoints)` | correcto |
| `BESS/SistemaBESS.py` | corregido en la vuelta anterior: límite de corriente por tensión, no por temperatura | corregido |

## Discrepancias encontradas

### A1 · `Demanda`: el archivo y la clase están en módulos distintos
El manuscrito dice «(`Demanda/SistemaDemanda.py`), en el que una única clase `PerfilDemanda` lee una serie temporal normalizada». En el repositorio, `SistemaDemanda.py` contiene la clase `SistemaDemanda` y `PerfilDemanda` vive en `Demanda/PerfilDemanda.py`. La frase describe el comportamiento correcto pero atribuye la clase al archivo equivocado.

### A2 · `Diesel`: el módulo se llama `Diesel.py` y la constante no se llama `T_eng`
El manuscrito cita `Diesel/SistemaDiesel.py`; el archivo es `Diesel/Diesel.py`. La clase es `MotorDiesel` y su constructor declara `Ke=1.0, te=0.035`, es decir una constante de tiempo de **35 ms** que el texto describe como «constante de transporte del motor térmico $T_{eng}$». El concepto existe; el nombre del archivo, el de la constante y probablemente el valor deben alinearse. **No se encontró `T_act`** en el módulo: la constante del actuador de combustible que el texto declara no aparece con ese nombre.

### A3 · `Solar`: el condensador de bus de 10 000 µF no aparece en el módulo
El texto afirma `C_dc = 10 000 µF` para el modelo fotovoltaico. No hay `C_dc` ni `10000` en `Solar/SistemaSolar.py`; `common/GridInverter.py` declara `Vdcref=400.0` pero no la capacidad. Puede estar en otra capa, pero la afirmación no se sostiene donde el texto la ubica.

### A4 · `Hidrica`: la constante de la columna de agua no aparece
El texto cita `Hidrica/SistemaHidrico.py` con $T_w$ y función de transferencia servogobernada. El directorio `Hidrica/` existe, pero `T_w` no aparece en ningún `.py` del proyecto. Requiere inspección del módulo antes de corregir.

## Lo que falta para cerrar el paso 1

1. Abrir `Hidrica/` y localizar cómo se modela la columna de agua y con qué nombre de constante.
2. Abrir `Diesel/Diesel.py` y determinar si existe un actuador de primer orden (el `te=0.035`) y si hay una segunda constante (el `T_act` del texto).
3. Rastrear `C_dc` en todo el proyecto para saber si la capacidad del bus se declara en el conmutador o en el recurso.
4. Repetir el barrido sobre frases operativas que **no** nombran archivo (buffer de frescura, proxy de red, antichattering) y contrastarlas con `Agents/` y `Central_PC/`.

**Regla que confirma esta pasada:** el nombre del archivo y el de la constante son parte de la afirmación. Una frase puede describir bien el comportamiento y aun así ser falsa en la referencia, y eso se verifica abriendo el código, no leyendo el capítulo.
