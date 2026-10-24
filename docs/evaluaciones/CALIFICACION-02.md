# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Kevin Grajales · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `c99804f`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 14 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 18 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre 10 y 50 elementos y dice que faltan tamaños intermedios para precisarlo.
- Compara bien con el máximo de un arreglo: recurrencia `T(n) = 2T(n/2) + Θ(1)`, resultado `Θ(n)`, igual que recorrer una vez.
- Da una estimación para 1.000.000 de registros y declara que es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 5 nunca dice de forma explícita qué algoritmo recomienda a la gerente. Las cifras (15,7 horas contra 5 segundos) lo sugieren, pero la recomendación debía escribirse y justificarse.
- En la pregunta 4 falta decir que el costo de combinar es constante y por eso dividir no ayuda, frente a lo que sí pasa en el subarreglo (combinar cuesta `Θ(n)`).

## 2. Calidad de la explicación teórica (14 / 20)
**Lo que hizo bien:**
- La recurrencia `T(n) = 2T(n/2) + Θ(n)` es correcta y se resuelve con el método maestro (caso 2, `Θ(n log n)`).

**Lo que puede mejorar:**
- Explique de dónde sale cada término con más detalle: por qué dos subproblemas, por qué de tamaño `n/2` y por qué el caso cruzado cuesta `Θ(n)`.
- Al verificar la condición del caso 2, escriba la comparación completa entre `f(n)` y `n^(log_b a)`.
- El `Θ(n²)` de la fuerza bruta se afirma en una frase. Falta mostrar el conteo de pares de días (`n(n+1)/2`) que lo justifica.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos, no llama a la fuerza bruta y no modifica la lista recibida.
- Tiene type hints y docstrings en las funciones.

**Lo que puede mejorar:**
- En `pruebas.py` faltan las dos líneas en blanco entre funciones (PEP 8).

## 4. Calidad del análisis de las gráficas (18 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños (hasta 4000).
- Calcula el factor de crecimiento al duplicar `n` para los dos algoritmos.

**Lo que puede mejorar:**
- Los factores del informe no se apoyan en la gráfica publicada. En ella la fuerza bruta pasa de cerca de 0,26 s (n = 2000) a cerca de 0,91 s (n = 4000), un factor cercano a 3,5, y no 4,11 como dice el texto.
- No contrasta los números con lo que predice la teoría (cerca de 4 para `n²` y algo más de 2 para `n log n`). Decir solo "son compatibles" no basta: el 2,77 de divide y vencerás está bastante por encima de lo esperado y merecía comentario.
- No indica si repitió las mediciones (se sugiere promediar varias corridas).

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Carpeta `lab2-divide-y-vencer/` con todos los archivos del entregable, la gráfica se ve en el informe, el código está enlazado y hay varios commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción no mencionan cómo activar el entorno virtual ni instalar `matplotlib` desde `requirements.txt`.
- La nota de la Parte 2 no dice cómo midió más allá de `perf_counter` (por ejemplo, repeticiones).

## ¿El código funciona?
Sí. Las pruebas pasan y las dos soluciones coinciden con un cálculo de referencia en cientos de listas aleatorias. La medición corre y genera la gráfica.

## Para el próximo laboratorio
- Escriba una recomendación clara y justificada al final del análisis.
- Muestre los cálculos paso a paso (conteo de pares, verificación del método maestro).
- Calcule los factores de crecimiento leyendo los valores de su propia gráfica y compárelos con el valor teórico.
- Agregue una tabla con los tiempos medidos y repita cada medición para reducir el ruido.
- Deje dos líneas en blanco entre funciones e indique cómo activar el entorno.
