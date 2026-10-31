"""Pruebas de las estructuras de consulta de guias."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista() -> None:
    lista = ListaEnlazada()
    lista.insertar(1234567890, "en bodega")
    lista.insertar(1234567891, "en reparto")
    assert lista.buscar(1234567890) == "en bodega"
    assert lista.buscar(1234567891) == "en reparto"
    assert lista.buscar(9999999999) is None
    assert lista.tamano == 2


def probar_colisiones() -> None:
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_coincidencia_aleatoria() -> None:
    azar = random.Random(42)
    for _ in range(20):
        cantidad = azar.randint(1, 60)
        guias = azar.sample(range(1_000_000_000, 1_000_001_000), cantidad)
        lista = ListaEnlazada()
        tabla = TablaHash(17)
        estados = {}

        for guia in guias:
            estado = azar.choice(
                ["en bodega", "en reparto", "entregado"]
            )
            estados[guia] = estado
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)
            assert lista.buscar(guia) == estados[guia]

        inexistentes = azar.sample(
            [g for g in range(1_000_002_000, 1_000_003_000)
             if g not in estados],
            10,
        )
        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None


if __name__ == "__main__":
    probar_lista()
    probar_colisiones()
    probar_coincidencia_aleatoria()
    print("Pruebas de lista: OK")
    print("Pruebas de colisiones y factor de carga: OK")
    print("Pruebas aleatorias (20 colecciones): OK")
    print("Todas las pruebas finalizaron correctamente.")
