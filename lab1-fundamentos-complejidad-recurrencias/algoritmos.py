
"""Algoritmos de ordenamiento para los índices de riesgo de Tamiza."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena índices de riesgo de mayor a menor mediante inserción.

    Args:
        datos: Lista de índices de riesgo que se van a ordenar.

    Returns:
        Una tupla con la lista ordenada y el número de comparaciones
        entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if lista[j] < actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break

        lista[j + 1] = actual

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena índices de riesgo de mayor a menor mediante Merge Sort.

    Args:
        datos: Lista de índices de riesgo que se van a ordenar.

    Returns:
        Una tupla con la lista ordenada y el número total de
        comparaciones entre elementos realizadas.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])

    resultado, comparaciones_merge = merge(izquierda, derecha)

    comparaciones_totales = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_merge
    )

    return resultado, comparaciones_totales


def merge(
    izquierda: list[int],
    derecha: list[int],
) -> tuple[list[int], int]:
    """Combina dos listas ordenadas de mayor a menor.

    Args:
        izquierda: Primera lista ordenada de mayor a menor.
        derecha: Segunda lista ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada y el número de comparaciones
        entre elementos de ambas listas.
    """
    resultado = []
    comparaciones = 0

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado, comparaciones
