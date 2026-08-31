def calcular_promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        numeros: Lista de valores numéricos.

    Returns:
        El promedio de los valores de la lista.
    """
    suma = 0

    for numero in numeros:
        suma = suma + numero

    return suma / len(numeros)


def main() -> None:
    """Ejecuta el cálculo del promedio de una lista de ejemplo."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)

    print(promedio)


if __name__ == "__main__":
    main()