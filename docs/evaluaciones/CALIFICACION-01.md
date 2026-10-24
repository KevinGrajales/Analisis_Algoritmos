# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Kevin Grajales · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-24 23:59 · **Versión revisada:** commit `c99804f`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue dentro de las cuatro horas, y explica por qué duplicar el servidor solo divide el tiempo a la mitad sin cambiar el crecimiento cuadrático.
- En la Parte 2 identifica dos afectados (el paciente y el operador del centro de contacto) y dice quién asume el costo en cada caso.
- Discute que el orden de la lista decide a quién se llama primero, y habla de empates y validación de datos.

**Lo que puede mejorar:**
- El segundo ejemplo (proceso ETL de unos 70.000 registros) no dice qué restricción concreta se incumple; usted mismo aclara que no es un caso de incumplimiento. Debía ser un caso donde un algoritmo correcto resulte inviable, con datos y límite claros.
- La relación entre tiempo de ejecución y energía queda general: no hay una cifra ni un ejemplo de cómo se acumula en años.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio, justifica usar el peor caso por la ventana estricta y deja la predicción escrita antes del experimento.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y aplica el método maestro verificando que `f(n)` es del mismo orden que `n^(log_2 2)`.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- Para insertion sort el análisis se hace por operaciones (ciclo, comparaciones, desplazamientos) y no línea por línea de su código con el costo de cada una.
- En la definición del caso promedio falta decir que se toma sobre todas las entradas posibles de tamaño fijo, con qué distribución.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no tocan la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. La mezcla es propia.
- Los generadores devuelven listas del tamaño pedido, sin repetidos, con semilla.

**Lo que puede mejorar:**
- Las funciones de `datos.py` y las de medición solo tienen una línea de explicación; faltan las secciones `Args` y `Returns` del estilo Google.
- Hay tres líneas en blanco seguidas entre funciones en `parte4_complejidad.py`, y una variable sin usar (`comparaciones`) en `medir_merge_sort`.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y se ven en el informe.
- Identifica con datos que el inverso es el peor caso, el casi ordenado el mejor y el aleatorio el intermedio, y contrasta con su predicción.
- La Parte 4.2 concluye que merge sort es mucho mejor y lo relaciona con las complejidades calculadas.
- La extrapolación a 1.200.000 registros está bien razonada y declarada como estimación (cerca de 26 horas contra unos 6 segundos).

**Lo que puede mejorar:**
- No explica qué pasa con los tamaños pequeños en la gráfica de la Parte 4 (en la lectura de n = 100 las dos curvas casi se tocan).
- En el concepto para la Secretaría no explica con qué criterio resolvió el compromiso de no mantener tres implementaciones, y la respuesta al servidor doble se apoya en la extrapolación más que en un valor leído de una gráfica citada.
- La consideración de memoria de merge sort es muy breve.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `lab1-fundamentos-complejidad-recurrencias/` tiene todos los archivos pedidos, las gráficas se ven y hay seis commits descriptivos.
- Hay nombre, instrucciones de reproducción y enlaces al código.

**Lo que puede mejorar:**
- Los enlaces al código están todos al inicio del informe; debían aparecer también al comienzo de la Parte 3 y de la Parte 4.
- Las instrucciones asumen Windows y un entorno virtual llamado `venv`.

## ¿El código funciona?
Sí. Ambos scripts corren sin errores, ordenan correctamente los tres escenarios y generan las gráficas.

## Para el próximo laboratorio
- Escoja ejemplos propios con cifras y una restricción clara (tiempo, memoria o latencia).
- Cuando se pida un análisis línea por línea, escriba cada línea del código con el número de veces que se ejecuta.
- Complete los *docstrings* con `Args` y `Returns` en todas las funciones.
- Enlace el código al comienzo de cada parte práctica y cite la gráfica y el tamaño del que toma cada dato.
- Explique siempre lo que se ve en tamaños pequeños cuando las curvas no se comportan como en la teoría.
