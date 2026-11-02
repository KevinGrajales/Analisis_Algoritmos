# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Kevin Grajales · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `9becb83` (rama `lab3-entrega`)

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 2 / 20 |
| Calidad de la explicación teórica | 1 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 12 / 25 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **41 / 100** |
| **Nota (0–5)** | **2.05** |

**Incumplimiento de convención:** No siguió la entrega acordada. El laboratorio no está en la rama `main`: se subió a una rama aparte llamada `lab3-entrega`, y en `main` no hay ninguna carpeta `lab3-estructuras-datos/`. Además, dentro de esa rama los archivos (`estructuras.py`, `pruebas.py`, `medicion.py`, `README.md` y `graficas/`) quedaron sueltos en la raíz del repositorio, sin la carpeta `lab3-estructuras-datos/`, y esa rama ni siquiera contiene sus laboratorios anteriores. La calificación se hizo con lo publicado en esa rama.

## 1. Corrección conceptual (2 / 20)
**Lo que hizo bien:**
- El informe menciona los datos del ejemplo (guías 10, 24 y 17 con m = 7) y las alturas aproximadas del árbol degenerado y del equilibrado.

**Lo que puede mejorar (y cómo corregirlo):**
- La Parte 3 del `README.md` no contiene respuestas: es una lista de indicaciones sobre lo que se debía contestar. No explica qué es una colisión, no compara encadenamiento con direccionamiento abierto, no justifica por qué la tabla no sirve para rangos, no calcula la altura ni las comparaciones del árbol y no da una estimación para 5.000.000 de envíos.
  → *Cómo corregirlo:* reemplace cada indicación por un párrafo propio que responda la pregunta correspondiente de la rúbrica (3, 4 y 5), usando sus propias palabras y sus mediciones.
- La recomendación para operaciones aparece dicha como indicación, sin razones ni cifras.
  → *Cómo corregirlo:* escriba qué estructura recomienda para cada necesidad, por qué, y declare como estimación el tiempo a 5.000.000 de guías explicando qué forma tiene la curva de cada estructura.

## 2. Calidad de la explicación teórica (1 / 20)
**Lo que hizo bien:**
- Reconoce que deben tratarse el supuesto de distribución uniforme y el caso de que todas las claves caigan en una casilla.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 1 no está respondida: solo aparece la lista de lo que debía explicar. No se justifica el costo `Θ(n)` de la lista ni el `Θ(1 + α)` de la tabla.
  → *Cómo corregirlo:* explique con sus palabras cuántas guías recorre cada estructura al buscar una guía que no existe, nombre el supuesto sobre la función hash y diga qué le pasaría a la tabla si todo cayera en una sola casilla.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` están bien hechas: la búsqueda usa un ciclo `while`, la tabla reutiliza la lista en cada casilla y no usa `dict`, `set` ni `hash()`.
- `pruebas.py` cubre búsqueda exitosa e infructuosa, la colisión de 10, 24 y 17 con m = 7 (casilla 3, longitud 3), el factor de carga 3/7 y 20 colecciones aleatorias donde lista y tabla coinciden. Todas las pruebas pasan.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, `medir_busquedas` no tiene *type hints* completos en `estructura` ni en el valor devuelto, y `construir_estructuras` no tiene *type hints* ni las secciones `Args` y `Returns`. `experimento_a` y `experimento_b` tampoco tienen `Args` y `Returns`.
  → *Cómo corregirlo:* agregue los tipos que faltan (por ejemplo `-> tuple[ListaEnlazada, TablaHash]`) y complete cada *docstring* con sus secciones `Args:` y `Returns:`.

## 4. Calidad del análisis de las gráficas (12 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen y se ven bien: tienen título, ejes rotulados y leyenda. La primera cubre seis valores de `n` (100 a 50.000) con ambas curvas en los mismos ejes y la segunda cuatro valores de `α` (0,5; 1; 4 y 10).
- Cronometró solo las búsquedas con `time.perf_counter()`, usó semillas fijas y `m` primo cercano a `n / 2`.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 2 no está respondida: no se calculan factores de crecimiento ni se compara con `Θ(n)`, `Θ(1)` y `Θ(1 + α)`. Tampoco se lee ningún valor de las gráficas.
  → *Cómo corregirlo:* escoja dos valores consecutivos de `n` de la primera gráfica, lea el tiempo de cada estructura, calcule cuántas veces se multiplicó y compárelo con lo que se esperaba. En la segunda gráfica, describa cómo cambia el tiempo al crecer `α`.
- En la segunda gráfica, el tiempo baja entre `α` = 0,5 y `α` = 4 antes de subir en `α` = 10. Eso no se comenta.
  → *Cómo corregirlo:* diga en el informe si esa forma coincide con lo esperado y a qué puede deberse (por ejemplo, el ruido al medir tiempos tan pequeños).

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- El `README.md` trae su nombre, sigue el orden pedido, enlaza `estructuras.py`, `pruebas.py` y `medicion.py`, e incrusta las dos gráficas con rutas que funcionan.
- Tiene cinco commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió la estructura de carpetas ni la rama acordadas (ver el incumplimiento de convención al inicio).
  → *Cómo corregirlo:* cree `lab3-estructuras-datos/` (o `laboratorios/lab3-estructuras-datos/`) en `main` y mueva allí los archivos con `git mv`.
- El informe no incluye las instrucciones para reproducir el experimento (cómo activar el entorno y qué comando ejecutar para las pruebas y para la medición).
  → *Cómo corregirlo:* agregue al inicio del `README.md` los pasos para activar el entorno y los comandos `python pruebas.py` y `python medicion.py`.
- El `README.md` conserva textos de la guía, como "Escribe las cinco respuestas con tus propias palabras", en lugar de la versión final del informe.
  → *Cómo corregirlo:* elimine esos textos de instrucción cuando escriba sus respuestas.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores, la lista y la tabla devuelven lo mismo, y la medición corre y genera las dos gráficas.
