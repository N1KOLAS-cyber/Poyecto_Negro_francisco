**Pseudocodigo del Algoritmo de Recorrido Merge Sort**

Funcion MergeSort(lista)  
    Si longitud(lista) > 1 Entonces  
        medio <- longitud(lista) / 2  
        izquierda <- lista[0:medio]  
        derecha <- lista[medio:fin]  

        MergeSort(izquierda)  
        MergeSort(derecha)  

        i <- 0, j <- 0, k <- 0  

        Mientras i < longitud(izquierda) y j < longitud(derecha) Hacer  
            Si izquierda[i] <= derecha[j] Entonces  
                lista[k] <- izquierda[i]  
                i <- i + 1  
            Sino  
                lista[k] <- derecha[j]  
                j <- j + 1  
            FinSi  
            k <- k + 1  
        FinMientras  

        Mientras i < longitud(izquierda) Hacer  
            lista[k] <- izquierda[i]  
            i <- i + 1  
            k <- k + 1  
        FinMientras  

        Mientras j < longitud(derecha) Hacer  
            lista[k] <- derecha[j]  
            j <- j + 1  
            k <- k + 1  
        FinMientras  
    FinSi  
FinFuncion  

=== **Pasos del Algoritmo** ===

--1. Inicio: Comenzamos con una lista desordenada:
lista = [38, 27, 43, 3, 9, 82, 10]

--2. División:
Dividimos la lista en dos mitades de forma recursiva hasta que cada sublista tenga un solo elemento.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio
        left = arr[:mid]  # Divide en dos mitades
        right = arr[mid:]

        merge_sort(left)  # Llamada recursiva a la mitad izquierda
        merge_sort(right)  # Llamada recursiva a la mitad derecha

--3. Fusión:
Comenzamos a combinar las sublistas ordenadas en una lista más grande, comparando los elementos de ambas mitades y colocando el menor primero.

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # Compara elementos
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):  # Si quedan elementos en la izquierda
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):  # Si quedan elementos en la derecha
            arr[k] = right[j]
            j += 1
            k += 1

--4. Repetición:
Se repiten los pasos de dividir y mezclar hasta que la lista esté completamente ordenada.

lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)

--5. Fin:
Imprimimos la lista ordenada.

print("Lista ordenada:", lista)

Salida esperada:

Lista ordenada: [3, 9, 10, 27, 38, 43, 82]
--Ejemplo 1: Mejor de los casos
(Cuando el arreglo ya está ordenado y cada división genera subarreglos equilibrados.)

Arreglo inicial: [1, 2, 3, 4, 5, 6, 7, 8]

Paso 1: División
Dividimos el arreglo en dos mitades:

Mitad izquierda: [1, 2, 3, 4]
Mitad derecha: [5, 6, 7, 8]
División recursiva de la mitad izquierda:

[1, 2, 3, 4] → [1, 2] y [3, 4]
[1, 2] → [1] y [2]
[3, 4] → [3] y [4]
División recursiva de la mitad derecha:

[5, 6, 7, 8] → [5, 6] y [7, 8]
[5, 6] → [5] y [6]
[7, 8] → [7] y [8]
Paso 2: Fusión
Fusión de [1] y [2]: → [1, 2]
Fusión de [3] y [4]: → [3, 4]
Fusión de [1, 2] y [3, 4]: → [1, 2, 3, 4]
Fusión de [5] y [6]: → [5, 6]
Fusión de [7] y [8]: → [7, 8]
Fusión de [5, 6] y [7, 8]: → [5, 6, 7, 8]
Fusión final de [1, 2, 3, 4] y [5, 6, 7, 8]: → [1, 2, 3, 4, 5, 6, 7, 8]

**Pseudocodigo del Algoritmo de Recorrido Merge Sort**

Funcion MergeSort(lista) Si longitud(lista) \> 1 Entonces medio \<-
longitud(lista) / 2 izquierda \<- lista\[0:medio\] derecha \<-
lista\[medio:fin\]

MergeSort(izquierda) MergeSort(derecha)

i \<- 0, j \<- 0, k \<- 0

Mientras i \< longitud(izquierda) y j \< longitud(derecha) Hacer Si
izquierda\[i\] \<= derecha\[j\] Entonces lista\[k\] \<- izquierda\[i\] i
\<- i + 1 Sino lista\[k\] \<- derecha\[j\] j \<- j + 1 FinSi k \<- k + 1
FinMientras

Mientras i \< longitud(izquierda) Hacer lista\[k\] \<- izquierda\[i\] i
\<- i + 1 k \<- k + 1 FinMientras

Mientras j \< longitud(derecha) Hacer lista\[k\] \<- derecha\[j\] j \<-
j + 1 k \<- k + 1 FinMientras FinSi FinFuncion

paso del algoritmo

\--1. Inicio: Comenzamos con una lista desordenada: lista = \[38, 27,
43, 3, 9, 82, 10\]

\--2. División: Dividimos la lista en dos mitades de forma recursiva
hasta que cada sublista tenga un solo elemento.

def merge_sort(arr): if len(arr) \> 1: mid = len(arr) // 2 \# Encuentra
el punto medio left = arr\[:mid\] \# Divide en dos mitades right =
arr\[mid:\]

merge_sort(left) \# Llamada recursiva a la mitad izquierda
merge_sort(right) \# Llamada recursiva a la mitad derecha

\--3. Fusión: Comenzamos a combinar las sublistas ordenadas en una lista
más grande, comparando los elementos de ambas mitades y colocando el
menor primero.

i = j = k = 0

while i \< len(left) and j \< len(right): if left\[i\] \<= right\[j\]:
\# Compara elementos arr\[k\] = left\[i\] i += 1 else: arr\[k\] =
right\[j\] j += 1 k += 1

while i \< len(left): \# Si quedan elementos en la izquierda arr\[k\] =
left\[i\] i += 1 k += 1

while j \< len(right): \# Si quedan elementos en la derecha arr\[k\] =
right\[j\] j += 1 k += 1

\--4. Repetición: Se repiten los pasos de dividir y mezclar hasta que la
lista esté completamente ordenada.

lista = \[38, 27, 43, 3, 9, 82, 10\] merge_sort(lista)

\--5. Fin: Imprimimos la lista ordenada.

print(\"Lista ordenada:\", lista)

Salida esperada:

Lista ordenada: \[3, 9, 10, 27, 38, 43, 82\]
