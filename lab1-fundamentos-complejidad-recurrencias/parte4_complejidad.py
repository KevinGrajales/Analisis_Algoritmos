"""Comparacion de insertion sort y merge sort."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def medir_insertion_sort(datos: list[int]) -> float:
    """Mide el tiempo de insertion sort."""
    inicio = time.perf_counter()

    insertion_sort(datos)

    fin = time.perf_counter()

    return fin - inicio



def medir_merge_sort(datos: list[int]) -> float:
    """Mide el tiempo de ejecución de Merge Sort."""
    inicio = time.perf_counter()

    _, comparaciones = merge_sort(datos)

    fin = time.perf_counter()

    return fin - inicio



def main() -> None:
    """Ejecuta la comparacion de los dos algoritmos."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanos:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_insertion_sort(datos)
        tiempo_merge = medir_merge_sort(datos)

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n}: "
            f"insertion sort={tiempo_insertion:.6f} segundos, "
            f"merge sort={tiempo_merge:.6f} segundos"
        )

    plt.figure()

    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        tamanos,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()

    plt.savefig("graficas/parte4_tiempo.png")
    

    plt.close()


if __name__ == "__main__":
    main()