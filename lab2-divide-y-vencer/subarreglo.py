
"""Subarreglo máximo: fuerza bruta y divide y vencerás."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de días.

    Args:
        valores: Variación diaria de caja, una por día. La lista
            debe tener al menos un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los índices inclusivos
        del tramo de mayor suma y el valor de esa suma.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for inicio in range(len(valores)):
        suma_actual = 0.0

        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_inicio = inicio
                mejor_fin = fin
                mejor_suma = suma_actual

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango considerado (inclusive).
        medio: Índice del último elemento de la mitad izquierda.
        fin: Índice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye
        al menos un elemento de cada mitad.
    """
    suma_actual = 0.0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]

        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    suma_actual = 0.0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]

        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    suma_total = mejor_suma_izquierda + mejor_suma_derecha

    return mejor_inicio, mejor_fin, suma_total


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha mediante divide y vencerás.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango a considerar (inclusive).
        fin: Índice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro del
        rango indicado.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izq_inicio, izq_fin, suma_izq = subarreglo_maximo(
        valores, inicio, medio
    )
    der_inicio, der_fin, suma_der = subarreglo_maximo(
        valores, medio + 1, fin
    )
    cruz_inicio, cruz_fin, suma_cruz = suma_cruzada(
        valores, inicio, medio, fin
    )

    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return izq_inicio, izq_fin, suma_izq

    if suma_der >= suma_izq and suma_der >= suma_cruz:
        return der_inicio, der_fin, suma_der

    return cruz_inicio, cruz_fin, suma_cruz
