"""Experimento de peor, mejor y caso promedio para insertion sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def medir_escenario(datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        datos: lista de datos que se va a ordenar.

    Returns:
        Una tupla con el tiempo en segundos y el número de comparaciones.
    """
    inicio = time.perf_counter()

    _, comparaciones = insertion_sort(datos)

    fin = time.perf_counter()

    tiempo = fin - inicio

    return tiempo, comparaciones


def main() -> None:
    """Ejecuta el experimento de la Parte 3."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    escenarios = {
        "Aleatorio": generar_aleatorio,
        "Casi ordenado": generar_casi_ordenado,
        "Inverso": generar_inverso,
    }

    tiempos = {}
    comparaciones = {}

    for nombre, generador in escenarios.items():
        tiempos[nombre] = []
        comparaciones[nombre] = []

        for n in tamanos:
            datos = generador(n)

            tiempo, cantidad_comparaciones = medir_escenario(datos)

            tiempos[nombre].append(tiempo)
            comparaciones[nombre].append(cantidad_comparaciones)

            print(
                f"{nombre} - n={n}: "
                f"{cantidad_comparaciones} comparaciones, "
                f"{tiempo:.6f} segundos"
            )

    plt.figure()
    plt.plot(
        tamanos,
        comparaciones["Aleatorio"],
        marker="o",
        label="Aleatorio",
    )
    plt.plot(
        tamanos,
        comparaciones["Casi ordenado"],
        marker="o",
        label="Casi ordenado",
    )
    plt.plot(
        tamanos,
        comparaciones["Inverso"],
        marker="o",
        label="Inverso",
    )

    plt.title("Insertion Sort: comparaciones por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.savefig(
        "lab1-fundamentos-complejidad-recurrencias/"
        "graficas/parte3_comparaciones.png"
    )
    plt.close()

    plt.figure()
    plt.plot(
        tamanos,
        tiempos["Aleatorio"],
        marker="o",
        label="Aleatorio",
    )
    plt.plot(
        tamanos,
        tiempos["Casi ordenado"],
        marker="o",
        label="Casi ordenado",
    )
    plt.plot(
        tamanos,
        tiempos["Inverso"],
        marker="o",
        label="Inverso",
    )

    plt.title("Insertion Sort: tiempo por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.savefig(
        "lab1-fundamentos-complejidad-recurrencias/"
        "graficas/parte3_tiempo.png"
    )
    plt.close()


if __name__ == "__main__":
    main()