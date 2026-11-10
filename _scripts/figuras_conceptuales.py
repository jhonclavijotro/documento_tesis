"""Tres figuras conceptuales del manuscrito: estructura, flujo de datos y mapa de validacion.

Salida: PDF vectorial, Type 42, ancho 14.81 cm (= 0.95\\textwidth), tipografia 6.4-7.4 pt.
Regeneracion:  python figuras_conceptuales.py     (requiere matplotlib)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

matplotlib.rcParams.update({
    "pdf.fonttype": 42, "ps.fonttype": 42, "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"], "font.size": 7.0,
})

OUT = r"D:\TEXTOS\TESIS\Figuras"
CM = 1 / 2.54
W_CM = 14.81


def canvas(h_cm):
    f = plt.figure(figsize=(W_CM * CM, h_cm * CM))
    ax = f.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    return f, ax


def block(ax, x, y, w, h, title, lines, fc="#f2f2f2", fs=6.6, tfs=7.4, step=6.2, pad_top=4.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.0",
                                linewidth=0.8, edgecolor="#333333", facecolor=fc))
    ax.text(x + w / 2, y + h - pad_top, title, ha="center", va="top",
            fontsize=tfs, fontweight="bold")
    for i, ln in enumerate(lines):
        ax.text(x + 2.0, y + h - pad_top - 6.4 - i * step, ln, ha="left", va="top", fontsize=fs)


def arrow(ax, p, q, style="-|>", ls="-", rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=7.5,
                                 linewidth=0.75, color="#333333", linestyle=ls,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=1.5, shrinkB=1.5))


def note(ax, x, y, s, fs=6.4, ha="center", weight="normal"):
    ax.text(x, y, s, ha=ha, va="center", fontsize=fs, fontweight=weight)


def estructura():
    f, ax = canvas(9.6)
    block(ax, 1.0, 55, 42, 43, "Borde: agentes en Raspberry Pi 5 (\u00d76)", [
        "Agents/distributed_node_runner.py",
        "Agents/fixed_time_consensus.py",
        "Agents/node_dynamic_process.py",
        "Agents/network_impairment_proxy.py",
        "Agents/monitor_node_service.py",
    ], fc="#e9f0f7")
    block(ax, 57.0, 55, 42, 43, "PC Central: orquestador 10.0.0.156", [
        "Central_PC/master_clock_zmq.py",
        "Central_PC/power_flow_clock_server.py",
        "Central_PC/power_flow_fbs.py",
        "Central_PC/sensitivity_matrices.py",
        "Central_PC/communication_emulator.py",
    ], fc="#e9f0f7")
    block(ax, 1.0, 31, 42, 18, "Recursos modelados (planta)", [
        "Diesel/   Solar/   BESS/",
        "Demanda/multi_load_process.py",
    ], fc="#f7f7f7", step=6.0)
    block(ax, 57.0, 31, 42, 18, "Interfaz y monitoreo", [
        "GUI/gui_command_center.py",
        "GUI/mqtt_publisher.py  \u00b7  dashboard HTTP",
    ], fc="#f7f7f7", step=6.0)
    block(ax, 1.0, 2.0, 98.0, 23.0, "Datos, escenarios y evaluaci\u00f3n", [
        "Forms/escenarios_generados/ESC-HIL-00x/   datos_meteorologicos \u00b7 datos_demanda \u00b7 topologia \u00b7 contingencias_telematicas",
        "outputs/benchmark/   harness \u00b7 metrics_v2 \u00b7 results/<run_id> \u00b7 CURRENT.json",
        "output_data/telemetry_monitor_cluster_8nodes_hil.csv",
    ], fc="#fbf6ea", step=5.4)

    arrow(ax, (43.0, 86), (57.0, 86))
    arrow(ax, (57.0, 76), (43.0, 76))
    note(ax, 50, 92.5, "ZeroMQ")
    note(ax, 50, 89.0, "lock-step")
    note(ax, 50, 73.0, "$V$ pu, $f$")
    arrow(ax, (22.0, 55), (22.0, 49.0))
    note(ax, 24.5, 52.0, "consigna", ha="left")
    arrow(ax, (22.0, 40), (22.0, 47.0))
    arrow(ax, (78.0, 49), (78.0, 40))
    arrow(ax, (22.0, 31), (22.0, 25.0))
    arrow(ax, (78.0, 31), (78.0, 25.0))
    f.savefig(os.path.join(OUT, "fig_estructura.pdf")); plt.close(f)


def flujo():
    f, ax = canvas(9.0)
    block(ax, 1.0, 52, 29, 40, "Nodo DER $i$ (borde)", [
        "runner del agente",
        "ley FxTS",
        "micro-paso $h$ = 1 ms",
        "retenedor ZOH",
    ], fc="#e9f0f7")
    block(ax, 35.5, 52, 29, 40, "Enlace de comunicaci\u00f3n", [
        "ZeroMQ REQ/REP",
        "latencia \u00b7 p\u00e9rdida",
        "desconexi\u00f3n de enlace",
        "\u00faltimo estado conocido",
    ], fc="#f7f7f7")
    block(ax, 70.0, 52, 29, 40, "PC Central", [
        "servidor maestro",
        "lock-step $H$ = 0.5 s",
        "flujo de potencia (FBS)",
        "matrices de sensibilidad",
    ], fc="#e9f0f7")
    note(ax, 50, 95.0, "consigna   $P_{\\mathrm{ref}},\\ Q_{\\mathrm{ref}}$   \u2192", fs=6.6)
    arrow(ax, (30.0, 88), (35.5, 88))
    arrow(ax, (64.5, 88), (70.0, 88))
    arrow(ax, (70.0, 63), (64.5, 63))
    arrow(ax, (35.5, 63), (30.0, 63))
    note(ax, 50, 47.5, "\u2190   $P_i,\\ Q_i$ inyectadas  y  $V_{\\mathrm{pcc}}$ de retorno", fs=6.6)
    block(ax, 1.0, 30, 98, 16, "Plano de monitoreo \u2014 no participa del lazo de control", [
        "MQTT desde la interfaz (GUI/mqtt_publisher.py): telemetr\u00eda, registro y tablero",
    ], fc="#fbf6ea", step=5.0)
    block(ax, 1.0, 8, 98, 18, "Tiempos del lazo", [
        "micro-paso $h$ = 1 ms dentro del nodo   \u00b7   macro-paso $H$ = 0.5 s en el PC Central (2 Hz)",
        "retenedor de orden cero entre macro-pasos   \u00b7   consenso evaluado una vez por macro-paso",
    ], fc="#f7f7f7", step=5.6)
    arrow(ax, (84.0, 52), (84.0, 46), ls=(0, (2, 2)))
    f.savefig(os.path.join(OUT, "fig_flujo_datos.pdf")); plt.close(f)


def validacion():
    f, ax = canvas(8.8)
    block(ax, 1.0, 66, 42, 32, "Nivel T1: benchmark num\u00e9rico", [
        "9 variantes de control \u00b7 semilla 42",
        "8 gates (G1\u2013G8) \u00b7 corrida can\u00f3nica",
        "planta algebraico-cinem\u00e1tica (D-13)",
    ], fc="#e9f0f7")
    block(ax, 57.0, 66, 42, 32, "Nivel T2: banco f\u00edsico HIL", [
        "6 Raspberry Pi 5 + PC Central",
        "300 s a 2 Hz \u00b7 8 barras de 400 V",
        "tres familias de evaluaci\u00f3n (D-24)",
    ], fc="#e9f0f7")
    block(ax, 1.0, 22, 31, 34, "Familia 1: d\u00e9ficit", [
        "ESC-HIL-001 / 003",
        "12.59 kW > 11.54 kW",
        "validada",
    ], fc="#e8f2e8")
    block(ax, 34.5, 22, 31, 34, "Familia 2: excedente", [
        "ESC-HIL-006 y 007",
        "holgura +2.9 a +3.5 kW",
        "ensayo pendiente",
    ], fc="#fdf3dd")
    block(ax, 68.0, 22, 31, 34, "Familia 3: fallas", [
        "latencia \u00b7 p\u00e9rdida \u00b7 corte",
        "50\u2013500 ms \u00b7 0\u201330 %",
        "en construcci\u00f3n",
    ], fc="#fbe7e5")
    arrow(ax, (78.0, 66), (78.0, 58))
    arrow(ax, (78.0, 58), (16.5, 58))
    arrow(ax, (16.5, 58), (16.5, 56))
    arrow(ax, (50.0, 58), (50.0, 56))
    arrow(ax, (83.5, 58), (83.5, 56))
    f.savefig(os.path.join(OUT, "fig_validacion.pdf")); plt.close(f)


if __name__ == "__main__":
    estructura(); flujo(); validacion()
    print("generadas en", OUT)
