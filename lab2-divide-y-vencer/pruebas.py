import random


"""Pruebas para los algoritmos de subarreglo máximo."""

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


def verificar_suma(
    valores: list[float],
    suma_esperada: float,
) -> None:
    """Comprueba que ambos algoritmos encuentren la suma esperada."""
    resultado_fb = subarreglo_fuerza_bruta(valores)
    resultado_dv = subarreglo_maximo(valores, 0, len(valores) - 1)

    assert resultado_fb[2] == suma_esperada, (
        f"Fuerza bruta: se esperaba {suma_esperada}, "
        f"se obtuvo {resultado_fb[2]}"
    )
    assert resultado_dv[2] == suma_esperada, (
        f"Divide y vencerás: se esperaba {suma_esperada}, "
        f"se obtuvo {resultado_dv[2]}"
    )


def probar_casos_conocidos() -> None:
    """Prueba diferentes tipos de listas."""
    verificar_suma([-3, 5, -2, 8, -6, 3, 9, -4], 17)
    verificar_suma([7], 7)
    verificar_suma([-8, -3, -5, -2], -2)
    verificar_suma([1, 2, 3, 4], 10)

    # El mejor subarreglo cruza el punto medio.
    verificar_suma([-10, 4, -1, 5, -1, 4, -10], 11)

    print("Pruebas de casos conocidos: OK")

def probar_casos_aleatorios() -> None:
    """Compara ambos algoritmos con listas aleatorias."""
    random.seed(42)

    for _ in range(20):
        cantidad = random.randint(1, 20)
        valores = []

        for _ in range(cantidad):
            valores.append(random.randint(-10, 10))

        resultado_fb = subarreglo_fuerza_bruta(valores)
        resultado_dv = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )

        assert resultado_fb[2] == resultado_dv[2], (
            f"Los resultados no coinciden para {valores}"
        )

    print("Pruebas aleatorias: OK")

if __name__ == "__main__":
    probar_casos_conocidos()
    probar_casos_aleatorios()
    print("Todas las pruebas ejecutadas finalizaron correctamente.")

