
"""Medición de tiempos de los algoritmos de subarreglo máximo."""

import random
import time
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempos() -> None:
    """Mide los tiempos y genera una gráfica comparativa."""
    random.seed(42)

    tamanos = [10, 50, 100, 500, 1000, 2000, 4000]
    tiempos_fb = []
    tiempos_dv = []

    for n in tamanos:
        valores = []

        for _ in range(n):
            valores.append(random.randint(-100, 100))

        inicio = time.perf_counter()
        resultado_fb = subarreglo_fuerza_bruta(valores)
        tiempo_fb = time.perf_counter() - inicio

        inicio = time.perf_counter()
        resultado_dv = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )
        tiempo_dv = time.perf_counter() - inicio

        assert resultado_fb[2] == resultado_dv[2], (
            f"Las sumas no coinciden para n = {n}"
        )

        tiempos_fb.append(tiempo_fb)
        tiempos_dv.append(tiempo_dv)

        print(f"Tamaño: {n}")
        print(f"  Fuerza bruta: {tiempo_fb:.6f} segundos")
        print(f"  Divide y vencerás: {tiempo_dv:.6f} segundos")
        print()

    plt.plot(tamanos, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(
        tamanos,
        tiempos_dv,
        marker="o",
        label="Divide y vencerás",
    )

    plt.title("Tiempo de ejecución: subarreglo máximo")
    plt.xlabel("Tamaño de entrada (n elementos)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/tiempo_vs_n.png")
    plt.show()


if __name__ == "__main__":
    medir_tiempos()
