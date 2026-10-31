"""Experimentos de tiempo para lista enlazada y tabla hash."""

import random
import time
import os

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def medir_busquedas(estructura, consultas: list[int], repeticiones: int = 3) -> float:
    """Devuelve el tiempo medio por búsqueda en segundos.

    Args:
        estructura: objeto con método buscar.
        consultas: guias que se consultaran.
        repeticiones: cuantas rondas de consultas se realizan.

    Returns:
        Tiempo promedio en segundos por consulta.
    """
    total = 0.0
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        total += time.perf_counter() - inicio
    return total / (repeticiones * len(consultas))


def construir_estructuras(guias: list[int], m: int):
    """Construye lista y tabla con los mismos datos."""
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    azar = random.Random(100)
    estados = []
    for guia in guias:
        estado = azar.choice(["en bodega", "en reparto", "entregado"])
        estados.append(estado)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    # Comprobación de consistencia con una muestra de claves existentes.
    for guia in guias[:min(25, len(guias))]:
        assert lista.buscar(guia) == tabla.buscar(guia)
    return lista, tabla


def experimento_a() -> tuple[list[int], list[float], list[float]]:
    """Mide lista frente a tabla para distintos tamaños."""
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    for n in tamanos:
        azar = random.Random(2026 + n)
        guias = azar.sample(range(10**9, 10**10), n)
        m = 2 * n + 1
        # m es impar y cercano a n/2 en factor de carga (alpha ≈ 0.5).
        # El enunciado pide alpha alrededor de 2: elegimos m primo cercano n/2.
        m = max(3, n // 2)
        while any(m % divisor == 0 for divisor in range(2, int(m**0.5) + 1)):
            m += 1

        lista, tabla = construir_estructuras(guias, m)
        consultas = generar_guias_inexistentes(set(guias), 200, semilla=7 + n)
        tiempos_lista.append(medir_busquedas(lista, consultas))
        tiempos_tabla.append(medir_busquedas(tabla, consultas))
        print(
            f"n={n:>6} | m={m:>6} | alpha={tabla.factor_carga():.3f} | "
            f"lista={tiempos_lista[-1]:.9f} s | "
            f"tabla={tiempos_tabla[-1]:.9f} s"
        )

    os.makedirs("graficas", exist_ok=True)
    plt.figure()
    plt.plot(tamanos, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, marker="o", label="Tabla hash")
    plt.title("Búsqueda de guías inexistentes: lista vs. tabla hash")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()
    return tamanos, tiempos_lista, tiempos_tabla


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide el tiempo de búsqueda al variar el factor de carga."""
    n = 20000
    azar = random.Random(2027)
    guias = azar.sample(range(10**9, 10**10), n)
    alfas_deseados = [0.5, 1.0, 4.0, 10.0]
    alfas_medidos = []
    tiempos = []

    for alfa in alfas_deseados:
        m_aprox = max(3, round(n / alfa))
        m = m_aprox
        while any(m % divisor == 0 for divisor in range(2, int(m**0.5) + 1)):
            m += 1

        _, tabla = construir_estructuras(guias, m)
        consultas = generar_guias_inexistentes(set(guias), 200, semilla=500 + int(alfa * 10))
        tiempo = medir_busquedas(tabla, consultas)
        alfa_real = tabla.factor_carga()
        alfas_medidos.append(alfa_real)
        tiempos.append(tiempo)
        print(f"Experimento B | m={m} | alpha={alfa_real:.3f} | {tiempo:.9f} s")

    plt.figure()
    plt.plot(alfas_medidos, tiempos, marker="o", label="Tabla hash")
    plt.title("Efecto del factor de carga en la búsqueda")
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()
    return alfas_medidos, tiempos


if __name__ == "__main__":
    print("Experimento A: lista frente a tabla hash")
    experimento_a()
    print("\nExperimento B: efecto del factor de carga")
    experimento_b()
    print("\nGráficas guardadas en la carpeta graficas.")
