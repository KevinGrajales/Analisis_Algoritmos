# Laboratorio 01 — Fundamentos, complejidad y recurrencias

## Realizado por:

**Kevin Alejandro Grajales Camacho**

## Reproducción del experimento

El proyecto fue desarrollado en Python utilizando un entorno virtual y
matplotlib para las gráficas.

Para activar el entorno virtual desde la raíz del repositorio:

```powershell
.\venv\Scripts\Activate.ps1
```

Para ejecutar el experimento de la Parte 3:

```powershell
python .\lab1-fundamentos-complejidad-recurrencias\parte3_casos.py
```

Para ejecutar el experimento de la Parte 4:

```powershell
python .\lab1-fundamentos-complejidad-recurrencias\parte4_complejidad.py
```

Los resultados de las mediciones se muestran en la terminal y las
gráficas se guardan en la carpeta `graficas/`.

---

# Parte 1 — Analizar el algoritmo antes de comprar hardware

En el caso de Tamiza es importante diferenciar entre corrección y eficiencia respecto al tiempo. Un algoritmo es correcto si produce el resultado que se espera. En este caso, el ordenamiento es correcto si Tamiza entrega los índices de riesgo de mayor a menor, como lo requiere el sistema. Sin embargo, que el resultado sea correcto no significa que se obtenga dentro del tiempo disponible.

En este caso, Insertion Sort  debe realizar una gran cantidad de comparaciones y desplazamientos. Esto significa que cuando aumenta la cantidad de registros, el trabajo necesario puede crecer mucho más rápido que el tamaño de los datos. Por esta razón, el problema no se soluciona simplemente haciendo que el mismo algoritmo procese los datos un poco más rápido.

Segundo ejemplo: procesamiento ETL

Un ejemplo diferente que conozco por mis prácticas en la asignatura Inteligenica de negocios, es el procesamiento ETL de datos para cargarlos en SQL Server. En estas prácticas he trabajado con archivos que contienen muchos registros y que deben ser procesados, organizados y posteriormente cargados en una base de datos. Un proceso puede realizar correctamente las transformaciones y cargar los datos sin errores, pero aun así resultar inviable si tarda demasiado para la ventana de tiempo disponible.

Por ejemplo, si un proceso debe transformar y cargar aproximadamente 70.000 registros dentro de un tiempo determinado, podría entregar finalmente todos los datos correctamente y, aun así, incumplir la restricción si tarda más de ese tiempo. En este caso, la corrección del resultado y el tiempo necesario para obtenerlo son aspectos diferentes.
---

# Parte 2 — Responsabilidad ambiental y ética de la implementación

La elección de un algoritmo para Tamiza no solamente tiene consecuencias
sobre el tiempo de procesamiento. También implica considerar los recursos
computacionales utilizados y las consecuencias que puede tener un error
en el proceso.

Desde el punto de vista ambiental, un algoritmo que tarda más tiempo
mantiene el procesador y otros componentes del sistema trabajando durante
más tiempo. Si el proceso se ejecuta todas las madrugadas, ese consumo
se repite diariamente. Por lo tanto, una diferencia pequeña en una sola
ejecución puede convertirse en un consumo acumulado considerable después
de meses o años.

Desde el punto de vista ético, el resultado del ordenamiento tiene una
consecuencia directa porque determina el orden en que se contactan los
pacientes. Si el algoritmo no termina antes de la hora establecida, el
centro de contacto podría recibir una lista incompleta o incorrectamente
ordenada.

Un primer afectado sería el paciente. Si su registro queda fuera de la
lista o aparece en una posición incorrecta, podría retrasarse su
contacto para una valoración médica. En este caso, el costo del error
recae principalmente sobre el paciente, aunque también existe una
responsabilidad de la Secretaría y del equipo encargado del sistema.

Un segundo afectado sería el operador del centro de contacto. Si recibe
una lista incompleta o que no está ordenada correctamente, puede tener
que trabajar con información que no representa la prioridad establecida.
El operador asume el costo operativo del problema, aunque la causa
provenga del sistema.

Por esta razón, el algoritmo debe ser correcto tanto en el resultado
como en su capacidad para cumplir la restricción de tiempo. Además, el
ordenamiento debe ser confiable porque no solamente organiza datos:
determina quién será contactado primero.

---

# Parte 3 — Peor caso, mejor caso y caso promedio

## 3.1 — Explicación y predicción

El peor caso corresponde al conjunto de entradas que produce el mayor
costo de ejecución para un tamaño de entrada fijo. No significa
simplemente que sea una entrada "mala", sino que representa la entrada
que exige más trabajo entre las posibles entradas de ese tamaño.

El mejor caso corresponde al conjunto de entradas que produce el menor
costo de ejecución para un tamaño fijo.

El caso promedio representa el comportamiento esperado considerando las
posibles entradas de un tamaño determinado y su distribución. En este
laboratorio se utiliza el escenario aleatorio como aproximación
experimental al comportamiento promedio.

Para Tamiza, la decisión debe considerar principalmente el peor caso,
porque la ventana de procesamiento de cuatro horas es estricta. Un
algoritmo que funciona rápidamente en una entrada favorable pero puede
tardar demasiado cuando cambia la forma de los datos representa un
riesgo para un proceso que tiene una hora límite.

Antes de realizar las mediciones, la predicción para los tres escenarios
fue la siguiente:

- **Escenario A — Aleatorio:** caso promedio.
- **Escenario B — Casi ordenado:** mejor caso o un comportamiento cercano
  al mejor caso.
- **Escenario C — Inverso:** peor caso.

Esta predicción se basa en que Tamiza necesita ordenar los índices de
riesgo de mayor a menor. En el escenario B, el 98 % de los registros ya
se encuentra en el orden requerido y solamente el 2 % restante se
agrega al final. En el escenario C, los datos llegan exactamente en el
orden contrario al requerido.

---

## 3.2 — Demostración experimental

Se implementó `insertion_sort` sin utilizar `sorted()` ni `list.sort()`.
El algoritmo trabaja sobre una copia de la lista recibida y cuenta las
comparaciones entre elementos.

Los tamaños utilizados fueron:

```text
100, 200, 400, 800, 1600, 3200, 6400
```

Las mediciones obtenidas para el número de comparaciones fueron:

| Tamaño | Aleatorio | Casi ordenado | Inverso |
|---:|---:|---:|---:|
| 100 | 2.597 | 99 | 4.950 |
| 200 | 10.318 | 201 | 19.900 |
| 400 | 40.436 | 409 | 79.800 |
| 800 | 160.484 | 852 | 319.600 |
| 1600 | 648.481 | 1.843 | 1.279.200 |
| 3200 | 2.533.103 | 4.242 | 5.118.400 |
| 6400 | 10.276.753 | 10.649 | 20.476.800 |

### Análisis de los resultados

El escenario B presenta el menor número de comparaciones. Esto se debe
a que la mayor parte de los datos ya está organizada de acuerdo con el
orden que necesita Tamiza.

El escenario C presenta el mayor número de comparaciones. Para `n=6400`
se obtuvieron exactamente 20.476.800 comparaciones.

Esto confirma experimentalmente el comportamiento cuadrático del peor
caso de insertion sort.

El escenario A se encuentra entre los otros dos y presenta un
comportamiento representativo del caso promedio.

La predicción realizada antes de medir coincide con los resultados
experimentales:

- **Mejor caso:** B — Casi ordenado.
- **Caso promedio:** A — Aleatorio.
- **Peor caso:** C — Inverso.

### Comparaciones por escenario

![Comparaciones de Insertion Sort](graficas/parte3_comparaciones.png)

### Tiempo de ejecución por escenario

![Tiempo de ejecución de Insertion Sort](graficas/parte3_tiempo.png)

Las gráficas muestran que el comportamiento de los escenarios cambia
considerablemente a medida que aumenta el tamaño de entrada. El
escenario casi ordenado requiere mucho menos trabajo, mientras que el
escenario inverso presenta el mayor crecimiento.

---

# Parte 4 — Complejidad de Merge Sort e Insertion Sort

## 4.1 — Cálculo teórico

### Recurrencia de Merge Sort

Merge Sort divide el problema original en dos subproblemas de tamaño
aproximadamente `n/2`. Cada una de esas partes vuelve a ordenarse de
forma recursiva.

Después de ordenar las dos partes, se utiliza la operación `merge` para
combinarlas. 

### Método maestro

La forma general del método maestro es:

\[T(n)=aT(n/b)+f(n)\]

En este caso:

\[a=2\]

\[b=2\]

\[f(n)=\Theta(n)\]

Calculamos:

\[n^{\log_b a}=n^{\log_2 2}=n\]

Por lo tanto:

\[f(n)=\Theta(n)\]

y:

\[n^{\log_b a}=\Theta(n)\]

Ambas funciones tienen el mismo orden de crecimiento. Por lo tanto
corresponde al caso del método maestro en el que el costo de combinar
tiene el mismo orden que la parte recursiva.

El resultado es:

\[T(n)=\Theta(n\log n)\]

Por lo tanto, la complejidad temporal de Merge Sort es:

\[\boxed{\Theta(n\log n)}\]

---

## Complejidad de Insertion Sort

En la implementación utilizada, el ciclo externo recorre los elementos
desde la posición 1 hasta la última posición.

En el mejor caso, cuando los elementos ya están ordenados, el `while`
realiza solamente una comparación por cada elemento y después termina.
Por eso el número de comparaciones crece proporcionalmente con `n.

En el peor caso, cuando los datos están en orden inverso, el primer
elemento que se procesa realiza una comparación, el siguiente puede
realizar dos, el siguiente tres y así sucesivamente:

\[1+2+3+\cdots +(n-1)\]

La suma es:

\[\frac{n(n-1)}{2}\]

Por lo tanto:

\[T(n)=\Theta(n^2)\]

### Tabla de complejidades

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---|---|---|
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) |
| Merge Sort | Θ(n log n) | Θ(n log n) | Θ(n log n) |

---

## 4.2 — Validación experimental

Se compararon Insertion Sort y Merge Sort utilizando el escenario
aleatorio y los mismos tamaños de entrada de la Parte 3.

Los resultados obtenidos fueron:

| Tamaño | Insertion Sort (s) | Merge Sort (s) |
|---:|---:|---:|
| 100 | 0.002444 | 0.001026 |
| 200 | 0.004035 | 0.000968 |
| 400 | 0.022025 | 0.003891 |
| 800 | 0.092824 | 0.008642 |
| 1600 | 0.330407 | 0.016870 |
| 3200 | 1.017749 | 0.025374 |
| 6400 | 3.416150 | 0.040593 |

En `n=6400`, Insertion Sort tardó 3.416150 segundos, mientras que
Merge Sort tardó 0.040593 segundos.

La relación entre ambos tiempos en esta medición fue aproximadamente:

\[\frac{3.416150}{0.040593}\approx84.16\]

Por lo tanto, para este tamaño de entrada y en esta ejecución,
Merge Sort tardó aproximadamente 84 veces menos que Insertion Sort.

La diferencia aumenta a medida que crece el tamaño de entrada. Esto
coincide con el análisis teórico, porque Insertion Sort presenta un
crecimiento cuadrático en el caso promedio y Merge Sort presenta un
crecimiento de Θ(n log n).

### Comparación de tiempos

![Insertion Sort vs Merge Sort](graficas/parte4_tiempo.png)

La gráfica muestra que la curva de Insertion Sort aumenta rápidamente
cuando crece `n`, mientras que la curva de Merge Sort crece de forma
mucho más lenta. Para tamaños pequeños la diferencia puede ser menos
visible, pero al aumentar el tamaño de entrada la diferencia se hace
mucho más clara.

---

# 4.3 — Concepto técnico para la Secretaría de Salud

Para Tamiza utilizaría Merge Sort como algoritmo principal de
ordenamiento. La razón principal es que el canal de entrada puede
cambiar y el equipo no quiere mantener tres implementaciones distintas.
Insertion Sort puede comportarse muy bien cuando la entrada está casi
ordenada, como ocurre en el escenario B, pero su comportamiento cambia
de forma importante cuando los datos llegan en orden inverso.

Esto se observa en las mediciones realizadas. Para 6.400 registros, el
escenario casi ordenado necesitó solamente 10.649 comparaciones,
mientras que el escenario inverso necesitó 20.476.800. Esto representa
una diferencia muy grande en el trabajo realizado por el mismo
algoritmo.

En la comparación directa de algoritmos, para 6.400 registros
Insertion Sort tardó 3.416150 segundos y Merge Sort tardó 0.040593
segundos. En esa ejecución Merge Sort fue aproximadamente 84 veces más
rápido. La gráfica `parte4_tiempo.png` muestra que la diferencia entre
las curvas aumenta a medida que crece el tamaño de entrada.

Para los 1.200.000 registros de Tamiza, la siguiente comparación es una
estimación basada en las mediciones realizadas, no una medición directa.

Tomando el peor caso de Insertion Sort y extrapolando su comportamiento
cuadrático desde 6.400 registros:

\[t_{nuevo}\approx3.416150
\left(\frac{1.200.000}{6400}\right)^2\]

El resultado es aproximadamente:

\[120.300\text{ segundos}\]

es decir, alrededor de **33,4 horas**. Esta estimación supera ampliamente
la ventana disponible de cuatro horas.

Para Merge Sort, usando el comportamiento de crecimiento de
\(\Theta(n\log n)\) y tomando como referencia la medición de 6.400
registros:

\[t_{nuevo}\approx0.040593
\left(\frac{1.200.000\log_2(1.200.000)}
{6400\log_2(6400)}\right)\]

se obtiene una estimación aproximada de **12 segundos**. Esta cifra es
solamente una extrapolación y no reemplaza una prueba directa con
1.200.000 registros.

Con estos resultados, duplicar la velocidad del servidor no soluciona
el problema de fondo. En el peor caso medido, Insertion Sort necesitó
3.416150 segundos con solamente 6.400 registros. Si el problema
principal es el crecimiento cuadrático, aumentar la velocidad del
hardware solamente reduce el tiempo por una constante, mientras que el
crecimiento respecto al tamaño de los datos permanece.

También debe considerarse que Merge Sort utiliza memoria adicional para
realizar la combinación de las listas. Este costo debe tenerse en cuenta
en la infraestructura disponible. Sin embargo, para un proceso cuyo
volumen puede llegar a 1.200.000 registros y cuya ventana de ejecución
es estricta, el comportamiento temporal resulta una restricción crítica.

Por estas razones, para Tamiza utilizaría Merge Sort como algoritmo
general de ordenamiento, evitando depender de que los datos lleguen en
un escenario favorable.

---

# Conclusiones

El experimento permitió observar que el comportamiento de un algoritmo
de ordenamiento depende tanto del tamaño de entrada como de la
organización de los datos.

Insertion Sort presentó un comportamiento favorable cuando los datos
estaban casi ordenados, pero su costo aumentó considerablemente en el
escenario inverso. Para `n=6400`, este último escenario alcanzó
20.476.800 comparaciones.

La comparación con Merge Sort mostró una diferencia importante en los
tiempos de ejecución. Para `n=6400`, Insertion Sort tardó 3.416150
segundos frente a 0.040593 segundos de Merge Sort.

Los resultados experimentales son coherentes con el análisis teórico:
Insertion Sort puede llegar a Θ(n²), mientras que Merge Sort tiene un
crecimiento de Θ(n log n). Para un sistema como Tamiza, donde el tamaño
de los datos puede ser muy grande y existe una ventana de procesamiento
estricta, analizar la complejidad del algoritmo es fundamental antes de
decidir aumentar únicamente los recursos de hardware.