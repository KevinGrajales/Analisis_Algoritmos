def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
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

def merge_sort(datos: list[int]) -> list[int]:
    """Ordena una lista de menor a mayor usando merge sort.

    Args:
        datos: lista de datos que se va a ordenar.

    Returns:
        Una nueva lista con los datos ordenados.
    """
    if len(datos) <= 1:
        return datos

    mitad = len(datos) // 2

    izquierda = merge_sort(datos[:mitad])
    derecha = merge_sort(datos[mitad:])

    return merge(izquierda, derecha)


def merge(izquierda: list[int], derecha: list[int]) -> list[int]:
    """Combina dos listas ordenadas en una sola lista ordenada."""
    resultado = []

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
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

    return resultado