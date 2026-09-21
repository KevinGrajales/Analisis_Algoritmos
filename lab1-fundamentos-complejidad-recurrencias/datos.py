"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio."""
    random.seed(semilla)

    datos = list(range(n))
    random.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final."""
    random.seed(semilla)

    cantidad_nueva = int(n * 0.02)

    datos = list(range(n - 1, cantidad_nueva - 1, -1))

    nuevos = list(range(cantidad_nueva))
    random.shuffle(nuevos)

    return datos + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden inverso al requerido."""
    return list(range(n))