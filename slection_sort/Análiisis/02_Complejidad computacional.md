Karlos , Darla , Angel, Ian
## Mejor Caso (Best Case)

Este es el escenario más favorable para el algoritmo de 
ordenamiento por selección. Sin embargo, a diferencia de otros 
algoritmos, el mejor caso para el ordenamiento por selección 
no implica una reducción significativa en el número de operaciones. 
Incluso si la lista ya está ordenada en su totalidad, el algoritmo 
seguirá realizando la misma cantidad de comparaciones para verificar 
que cada elemento esté en su lugar.

PROCEDIMIENTO selection_sort (Vector a [1:n])
    PARA I VARIANDO DE 1 HASTA n - 1 HACER                         O(n)# Se ejecuta (n - 1) veces
        ENCONTRAR [j] EL ELEMENTO MÁS PEQUEÑO DE [i + 1:n];        O((n^2)/2)# Se ejecuta aproximadamente (n-i) veces
        INTERCAMBIAR [j] Y [i];                                    O(0)# no se ejecuta
FIN PROCEDIMIENTO;

Dado que el bucle exterior se ejecuta n-1 veces y el bucle implícito en la operación 
"ENCONTRAR" se ejecuta aproximadamente n-i veces en cada iteración del bucle exterior, 
la cantidad total de comparaciones es aproximadamente la suma de (n-1) + (n-2) + ... + 1,
lo que resulta en una complejidad de 𝑂(𝑛²). Incluso en el mejor caso, donde la lista 
ya está ordenada, todas estas comparaciones se realizan.

𝑇(𝑛) ≈ (𝑛 − 1) + (𝑛 − 2) + … + 1 = 𝑛(𝑛 − 1) / 2 = 𝑂(𝑛²)

**Complejidad Temporal:**
𝑂(𝑛²)

## Peor Caso (Worst Case)
Este es el escenario más desfavorable para el algoritmo. Se produce cuando la lista 
está completamente ordenada en orden inverso. En esta situación, el algoritmo 
realizará exactamente la misma cantidad de comparaciones que en el mejor caso o en 
cualquier otro caso, ya que siempre debe buscar el elemento más pequeño en la parte 
no ordenada de la lista. El número de intercambios también será el mismo.

PROCEDIMIENTO selection_sort (Vector a [1:n])
    PARA I VARIANDO DE 1 HASTA n - 1 HACER                         O(n)# Se ejecuta (n - 1) veces
        ENCONTRAR [j] EL ELEMENTO MÁS PEQUEÑO DE [i + 1:n];        O((n^2)/2)# Se ejecuta aproximadamente (n-i) veces
        INTERCAMBIAR [j] Y [i];                                     O(n)# Se ejecuta (n - 1) veces
FIN PROCEDIMIENTO;

Al igual que en el mejor caso, el bucle exterior se ejecuta n-1 veces, y la búsqueda 
del elemento más pequeño en la parte restante de la lista requiere aproximadamente n-i
comparaciones en cada iteración. Esto lleva a una complejidad temporal de 𝑂(𝑛²), 
incluso cuando la lista está en orden inverso.

𝑇(𝑛) ≈ (𝑛 − 1) + (𝑛 − 2) + … + 1 = 𝑛(𝑛 − 1) / 2 = 𝑂(𝑛²)

**Complejidad Temporal:**
𝑂(𝑛²)

## Caso Promedio (Average Case)
Este representa la situación más común en la ejecución del algoritmo. Se asume que 
los elementos del arreglo están en un orden aleatorio. En este caso, la cantidad de 
comparaciones realizadas por el algoritmo de ordenamiento por selección sigue siendo la 
misma que en el mejor y el peor caso. La posición inicial de los elementos no afecta la 
cantidad de comparaciones que se deben realizar para encontrar el mínimo en cada sublista.

PROCEDIMIENTO selection_sort (Vector a [1:n])
    PARA I VARIANDO DE 1 HASTA n - 1 HACER                         O(n)# Se ejecuta (n - 1) veces
        ENCONTRAR [j] EL ELEMENTO MÁS PEQUEÑO DE [i + 1:n];        O((n^2)/2)# En promedio, requiere un número de comparaciones similar a los otros casos
        INTERCAMBIAR [j] Y [i];                                    O(n)# Se ejecuta (n - 1) veces
FIN PROCEDIMIENTO;

𝑇(𝑛) ≈ (𝑛 − 1) + (𝑛 − 2) + … + 1 = 𝑛(𝑛 − 1) / 2 = 𝑂(𝑛²)

**Complejidad Temporal:**
𝑂(𝑛²)
