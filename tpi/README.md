Comparación de eficiencia entre suma recursiva y con bucle
Este script tiene como objetivo comparar el rendimiento (en tiempo de ejecución) entre dos métodos para sumar los elementos de una lista: uno usando recursión y otro usando un bucle for.

- Descripción del código
Importaciones necesarias:
Se importan librerías estándar como time, random y sys, junto con pandas y matplotlib para organizar y graficar los resultados.

- Configuración de recursión:
Se aumenta el límite de recursión (setrecursionlimit) para permitir llamadas recursivas con listas más grandes.

- Funciones principales:

_ suma_recursiva(lista): Suma los elementos de una lista usando recursión.

_ suma_loop(lista): Realiza la suma utilizando un bucle for.

_ tm(funcion, lista): Mide el tiempo que tarda una función en ejecutarse sobre una lista.

_ create_list(n): Genera una lista de tamaño n con números aleatorios entre 0 y 100.


- Generación de listas:
Se crean varias listas con diferentes tamaños (desde 10 hasta 2200 elementos) para probar el rendimiento de ambas funciones.

- Ejecución y medición:
Por cada lista, se mide el tiempo de ejecución tanto de la función recursiva como de la que usa bucle, y los resultados se almacenan en un DataFrame de pandas.

- Visualización de resultados:
Se grafica una comparación entre los tiempos de ambas funciones utilizando matplotlib.

- Salida esperada
Una tabla con los tiempos de ejecución por cada lista.
Un gráfico que muestra cómo varía el rendimiento según el tamaño de la lista, permitiendo observar cómo la recursividad puede volverse menos eficiente en listas grandes.

Link video presentación https://youtu.be/G23fAD_XRNU