**1. Inicio**

El algoritmo comienza con una lista de números desordenados. Veamos los
siguientes ejemplos:

Ejemplo 1:\
lista = \[7, 2, 6, 4\]

Ejemplo 2:\
lista = \[5, 2, 4, 6, 1, 3\]

**2. Comparación**

Se toma el segundo elemento de la lista como referencia y se compara con
los valores anteriores. Si el número es menor que alguno de ellos, se
desplazan los mayores hacia la derecha para abrir un espacio y ubicar el
elemento en su lugar correcto.

for j in range(1, len(lista)):\
key = lista\[j\]\
i = j - 1\
while i \>= 0 and lista\[i\] \> key:\
lista\[i + 1\] = lista\[i\] \# Movimiento de los valores\
i -= 1\
lista\[i + 1\] = key \# Inserción en la posición adecuada

**3. Proceso iterativo**

Este procedimiento se repite para cada elemento de la lista hasta
completar el ordenamiento.

Ejemplo 1 - Iteraciones detalladas\
Lista inicial: \[7, 2, 6, 4\]

Primera iteración:

Se toma 2 y se compara con 7.\
Como 7 es mayor, se mueve a la derecha.\
2 se coloca en su sitio.\
Resultado: \[2, 7, 6, 4\]

Segunda iteración:

6 se compara con 7.\
7 se mueve a la derecha.\
6 se ubica correctamente.\
Resultado: \[2, 6, 7, 4\]

Tercera iteración:

4 se compara con 7, 6 y 2.\
7 y 6 se desplazan hacia la derecha.\
4 se coloca en su lugar.\
Resultado: \[2, 4, 6, 7\]

**4. Continuación del proceso**

Se sigue este patrón hasta completar el ordenamiento de la lista.

Ejemplo 2 - Iteraciones detalladas\
Lista inicial: \[5, 2, 4, 6, 1, 3\]

Primera iteración:

2 se compara con 5.\
5 se mueve y 2 se inserta en su lugar.\
Resultado: \[2, 5, 4, 6, 1, 3\]

Segunda iteración:

4 se compara con 5.\
5 se desplaza y 4 se posiciona adecuadamente.\
Resultado: \[2, 4, 5, 6, 1, 3\]

Tercera iteración:

6 se compara con 5.\
Como 5 es menor, no hay cambios.\
Resultado: \[2, 4, 5, 6, 1, 3\]

Cuarta iteración:

1 se compara con 6, 5, 4, 2.\
Todos los números mayores se desplazan.\
1 se ubica en su posición correcta.\
Resultado: \[1, 2, 4, 5, 6, 3\]

Quinta iteración:

3 se compara con 6, 5, 4, 2.\
6, 5, 4 se mueven.\
3 se inserta en su sitio correcto.\
Resultado: \[1, 2, 3, 4, 5, 6\]

**5. Verificación**

Si en alguna de las iteraciones no se realizan movimientos, significa
que la lista ya está ordenada y el algoritmo puede detenerse antes de
recorrer todos los elementos.

for j in range(1, len(lista)):\
key = lista\[j\]\
i = j - 1\
swapped = False \# Indicador para verificar cambios\
while i \>= 0 and lista\[i\] \> key:\
lista\[i + 1\] = lista\[i\]\
i -= 1\
swapped = True \# Se ha realizado un movimiento\
lista\[i + 1\] = key\
if not swapped: \# Si no hubo cambios, la lista ya está ordenada\
break

1.  Finalización\
    Cuando todos los elementos han sido insertados en su posición
    correspondiente, la lista queda completamente ordenada.

Salida esperada:

Para Ejemplo 1:\
Lista ordenada: \[2, 4, 6, 7\]

Para Ejemplo 2:\
Lista ordenada: \[1, 2, 3, 4, 5, 6\]

def insertion_sort(lista):\
for j in range(1, len(lista)):\
key = lista\[j\]\
i = j - 1\
while i \>= 0 and lista\[i\] \> key:\
lista\[i + 1\] = lista\[i\] \# Desplazamiento\
i -= 1\
lista\[i + 1\] = key \# Inserción en la posición correcta\
print(f"Paso {j}: {lista}") \# Mostrar cada paso

return lista

**Ejemplo 1**

print("Ejemplo 1:")\
lista1 = \[7, 2, 6, 4\]\
print(f"Lista inicial: {lista1}")\
insertion_sort(lista1)\
print(f"Lista ordenada: {lista1}\\n")

**Ejemplo 2**

print("Ejemplo 2:")\
lista2 = \[5, 2, 4, 6, 1, 3\]\
print(f"Lista inicial: {lista2}")\
insertion_sort(lista2)\
print(f"Lista ordenada: {lista2}")

**Diagramas de flujo**

**EJEMPLO 1**

\[Inicio\]\
↓\
\[Mostrar lista inicial: \[7, 2, 6, 4\]\]\
↓\
\[Para j desde 1 hasta 3\]\
↓\
\[key = lista\[j\]\]\
↓\
\[i = j - 1\]\
↓\
\[¿i \>= 0 y lista\[i\] \> key?\] → Sí → \[Mover elemento: lista\[i +
1\] = lista\[i\]\]\
↓ ↓\
No \[Decrementar i: i = i - 1\]\
↓ ↓\
\[Insertar key: lista\[i + 1\] = key\] \[Volver a Comparar\]\
↓\
\[Mostrar paso actual: \[lista\]\]\
↓\
\[¿j == 3?\] → Sí → \[Mostrar lista ordenada: \[2, 4, 6, 7\]\]\
↓ ↓\
No \[Fin\]\
↓\
\[Volver al Bucle Principal\]

**EJEMPLO 2**

\[Inicio\]\
↓\
\[Mostrar lista inicial: \[5, 2, 4, 6, 1, 3\]\]\
↓\
\[Para j desde 1 hasta 5\]\
↓\
\[key = lista\[j\]\]\
↓\
\[i = j - 1\]\
↓\
\[¿i \>= 0 y lista\[i\] \> key?\] → Sí → \[Mover elemento: lista\[i +
1\] = lista\[i\]\]\
↓ ↓\
No \[Decrementar i: i = i - 1\]\
↓ ↓\
\[Insertar key: lista\[i + 1\] = key\] \[Volver a Comparar\]\
↓\
\[Mostrar paso actual: \[lista\]\]\
↓\
\[¿j == 5?\] → Sí → \[Mostrar lista ordenada: \[1, 2, 3, 4, 5, 6\]\]\
↓ ↓\
No \[Fin\]\
↓\
\[Volver al Bucle Principal\]
