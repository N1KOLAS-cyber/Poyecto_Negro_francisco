**Mejor Caso (Best Case)**

Este es el escenario más favorable para el algoritmo de ordenamiento por inserción. Se da cuando la lista ya está ordenada en su totalidad. En este caso, el algoritmo solo realiza un recorrido lineal por los elementos sin necesidad de realizar desplazamientos adicionales.

Complejidad Temporal:
𝑂(𝑛)

def insertion\_sort(arr):
for j in range(1, len(arr)): # Se ejecuta (n - 1) veces
key = arr[j] # Se ejecuta (n - 1) veces
i = j - 1 # Se ejecuta (n - 1) veces
while i >= 0 and arr[i] > key: # En el mejor caso, esta condición nunca se cumple (0 veces)
arr[i + 1] = arr[i] # No se realizan desplazamientos
i -= 1 # No hay decrementos en i
arr[i + 1] = key # Se ejecuta (n - 1) veces
Dado que en este caso el bucle while nunca se ejecuta, el tiempo total se puede expresar como:

𝑇(𝑛) = 𝑐₁(𝑛 − 1) + 𝑐₂(𝑛 − 1) + 𝑐₃(𝑛 − 1) + 𝑐₇(𝑛 − 1) = 𝑂(𝑛)

<a name="peor_caso_(worst_case)"></a>**Peor Caso (Worst Case)**

Este es el escenario más desfavorable para el algoritmo. Se produce cuando la lista está completamente ordenada en orden inverso. En esta situación, cada elemento debe ser desplazado hasta la primera posición, lo que genera el mayor número posible de comparaciones y movimientos dentro del arreglo.

Complejidad Temporal:
𝑂(𝑛²)

def insertion\_sort(arr):
for j in range(1, len(arr)): # Se ejecuta (n - 1) veces
key = arr[j] # Se ejecuta (n - 1) veces
i = j - 1 # Se ejecuta (n - 1) veces
while i >= 0 and arr[i] > key: # Se ejecuta aproximadamente n *(n - 1) veces
arr[i + 1] = arr[i] # Se ejecuta n* (n - 1) veces
i -= 1 # Se ejecuta n \* (n - 1) veces
arr[i + 1] = key # Se ejecuta (n - 1) veces
En este caso, el bucle while se ejecuta tantas veces como sea necesario para reordenar cada elemento, lo que produce un crecimiento cuadrático en el tiempo de ejecución.

𝑇(𝑛) = 𝑐₁(𝑛 − 1) + 𝑐₂(𝑛 − 1) + 𝑐₃(𝑛 − 1) + 𝑐₄,₅,₆(𝑛(𝑛 − 1)) + 𝑐₇(𝑛 − 1)

Por lo tanto, el tiempo de ejecución en el peor caso es 𝑂(𝑛²).

<a name="caso_promedio_(average_case)"></a>**Caso Promedio (Average Case)**

Este representa la situación más común en la ejecución del algoritmo. Se asume que los elementos del arreglo están en un orden aleatorio. En este caso, la cantidad de comparaciones y desplazamientos sigue un crecimiento cuadrático en promedio.

Complejidad Temporal:
𝑂(𝑛²)

def insertion\_sort(arr):
for j in range(1, len(arr)): # Se ejecuta (n - 1) veces
key = arr[j] # Se ejecuta (n - 1) veces
i = j - 1 # Se ejecuta (n - 1) veces
while i >= 0 and arr[i] > key: # En promedio, se ejecuta n/2 veces
arr[i + 1] = arr[i] # En promedio, ocurre n/2 veces
i -= 1
arr[i + 1] = key # Se ejecuta (n - 1) veces
En este caso, el número medio de comparaciones y desplazamientos se encuentra entre los valores del mejor y el peor caso, lo que lleva a la siguiente expresión matemática:

𝑇(𝑛) = 𝑐₁(𝑛 − 1) + 𝑐₂(𝑛 − 1) + 𝑐₃(𝑛 − 1) + 𝑐₄,₅,₆(𝑛²(𝑛 − 1)) + 𝑐₇(𝑛 − 1)

Dado que el término dominante es 𝑛², la complejidad sigue siendo 𝑂(𝑛²).

