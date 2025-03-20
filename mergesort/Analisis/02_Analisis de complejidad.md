\--Complejidad

Merge Sort tiene una complejidad temporal de O(n log n) va a estar en
todos los casos

\--Mejor de los casos (Best Case)

Complejidad en el mejor caso O(n log n).

\* Ocurre cuando el arreglo ya esta ordenado

\* Merge sort no evita las divisiones y fusiones aunque el arreglo este
ordenado

\* La única optimización posible es detectar que las mitades ya están
ordenadas y evitar fusionarlas, pero en general sigue realizando la
misma cantidad de operaciones.

\* Total: O(n log n)

\--Peor de los casos (Worst Case)

Complejidad en el peor caso O(n log n).

\* En cada nivel de la recursion, el arreglo se divide en dos mitades

\* En cada nivel, la operación merge toma O(n) tiempo total

\* Total: O(n log n)

Ejemplo de peor caso: Un arreglo ordenado en orden inverso, ya que de
todas formas Merge Sort realiza todas las divisiones y fusiones.

\-- Promedio de los casos (Average Case)

Complejidad en el caso promedio O(n log n).

\* Ocurre cuando el arreglo ya está ordenado.

\* Merge Sort no evita las divisiones y fusiones aunque el arreglo ya
esté ordenado.

\* La única optimización posible es detectar que las mitades ya están
ordenadas y evitar fusionarlas, pero en general sigue realizando la
misma cantidad de operaciones.

\* Total: O(n log n)

\--Calculo por linea del Pseudocodigo:

Funcion MergeSort(lista) \# O(n log n) Si longitud(lista) \> 1 Entonces
\# O(1) medio \<- longitud(lista) / 2 \# O(1) izquierda \<-
lista\[0:medio\] \# O(n) derecha \<- lista\[medio:fin\] \# O(n)

MergeSort(izquierda) \# O(n log n) MergeSort(derecha) \# O(n log n)

i \<- 0, j \<- 0, k \<- 0 \# O(1)

Mientras i \< longitud(izquierda) y j \< longitud(derecha) Hacer \# O(n)
Si izquierda\[i\] \<= derecha\[j\] Entonces \# O(1) lista\[k\] \<-
izquierda\[i\] \# O(1) i \<- i + 1 \# O(1) Sino lista\[k\] \<-
derecha\[j\] \# O(1) j \<- j + 1 \# O(1) FinSi k \<- k + 1 \# O(1)
FinMientras

Mientras i \< longitud(izquierda) Hacer \# O(n) lista\[k\] \<-
izquierda\[i\] \# O(1) i \<- i + 1 \# O(1) k \<- k + 1 \# O(1)
FinMientras

Mientras j \< longitud(derecha) Hacer \# O(n) lista\[k\] \<-
derecha\[j\] \# O(1) j \<- j + 1 \# O(1) k \<- k + 1 \# O(1) FinMientras

FinSi FinFuncion

\* Análisis de Complejidad de Merge Sort

T(n) = 2T(n/2) + O(n)

Total = c1(n) + c2(n-1) + c3(n log n) + c4(n-1) = O(n log n)

\# O(n log n) es la complejidad de la función.
