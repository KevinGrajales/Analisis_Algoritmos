# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Kevin Grajales · **Laboratorio:** Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `92231e1`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 25 |
| Calidad de la explicación teórica | 16 / 25 |
| Corrección de la implementación | 10 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **62 / 100** |
| **Nota (0–5)** | **3.10** |

## 1. Corrección conceptual (17 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo.
- En la Parte 2 identifica dos afectados (el paciente y el operador del centro de contacto) y dice quién asume el costo en cada caso.
- Explica que el consumo de energía se repite todas las madrugadas y se acumula.

**Lo que puede mejorar:**
- No nombra con claridad la restricción que se incumple (la ventana de cuatro horas con 1.200.000 registros).
- No explica bien por qué duplicar la velocidad del servidor no arregla el problema: falta decir que el trabajo crece con el cuadrado del tamaño y que el doble de velocidad solo lo reduce a la mitad.
- El segundo ejemplo (ETL con 70.000 registros) es flojo: no dice cuánto tiempo tarda ni cuál es el límite que se incumple, ni qué algoritmo lo hace inviable.
- La tensión de que el orden decide a quién se llama primero queda en una frase; falta desarrollarla.

## 2. Calidad de la explicación teórica (16 / 25)
**Lo que hizo bien:**
- Define los tres casos con claridad y justifica que para la ventana estricta se usa el peor caso.
- Escribe la predicción antes de medir y la compara después con los resultados.
- Aplica el método maestro identificando a, b y f(n), y llega a Θ(n log n). La tabla de complejidades está completa.

**Lo que puede mejorar:**
- La recurrencia de merge sort no está escrita completa (falta `T(n) = 2T(n/2) + Θ(n)`) ni se explica de dónde sale cada término, en especial el costo de combinar.
- En el método maestro falta nombrar el caso que aplica y escribir la condición que se verifica.
- Insertion sort no se analizó línea a línea: faltó indicar cuántas veces se ejecuta cada línea del código y sumar los costos. Solo contó comparaciones.

## 3. Corrección de la implementación (10 / 20)
**Lo que hizo bien:**
- `insertion_sort` ordena bien de mayor a menor, trabaja sobre una copia y cuenta las comparaciones correctamente.
- Los tres generadores producen lotes del tamaño pedido, sin repetidos y con semilla.
- No usa `sorted()` ni `list.sort()`.

**Lo que puede mejorar:**
- `merge_sort` no cumple lo pedido: devuelve solo la lista, no la cuenta de comparaciones. Su descripción dice "de menor a mayor" cuando en realidad ordena de mayor a menor.
- Falta la descripción de módulo en `algoritmos.py`, y `merge` y varias funciones auxiliares no tienen la sección de argumentos y retorno.
- Las descripciones de los generadores son más cortas que las pedidas.
- Faltan líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y están incrustadas en el informe.
- Identifica bien el mejor caso (B), el promedio (A) y el peor (C), con una tabla de datos.
- El concepto para la Secretaría recomienda merge sort, cita medidas (6.400 registros), extrapola a 1.200.000 registros declarando que es una estimación y menciona la memoria extra.

**Lo que puede mejorar:**
- No explica qué pasa con los tamaños pequeños en la gráfica de la Parte 4, ni compara con cuidado la forma de las curvas con las complejidades de 4.1.
- La respuesta a la compra del servidor debería usar el dato medido de forma más directa (por ejemplo, cuánto tiempo seguiría tardando insertion sort con el doble de velocidad).
- La estimación de insertion sort usa el tiempo del caso aleatorio como si fuera el peor caso; debe aclararlo o medir el caso inverso.
- Faltó discutir otra consideración, como la estabilidad o el mantenimiento del código.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- El informe está organizado por partes, con su nombre e instrucciones para reproducir los experimentos.
- Las gráficas se ven incrustadas con ruta relativa.

**Lo que puede mejorar:**
- No siguió la convención de nombres: el informe se llama `Readme.md` y debía llamarse `README.md`.
- Ninguna parte enlaza su código (`algoritmos.py`, `datos.py`, `parte3_casos.py`, `parte4_complejidad.py`).
- Solo hay 3 commits del laboratorio y se piden al menos 5, con avance repartido.

## ¿El código funciona?
Los scripts corren si se ejecutan desde la raíz del repositorio, como indica el informe, y ordenan bien. Si se ejecutan desde la carpeta del laboratorio fallan al guardar las gráficas. Las gráficas se generan, pero `merge_sort` no cuenta comparaciones.

## Para el próximo laboratorio
- Siga exactamente las firmas y descripciones que pide la guía (por ejemplo, que `merge_sort` devuelva también las comparaciones).
- Escriba la recurrencia completa y analice el código línea por línea, indicando cuántas veces se ejecuta cada una.
- Respalde cada argumento con números concretos (tiempos, cantidad de registros, ventana de cuatro horas).
- Enlace el código en cada parte, nombre el informe `README.md` y haga commits pequeños y frecuentes.
- Revise el estilo con una herramienta de PEP 8 antes de entregar.
