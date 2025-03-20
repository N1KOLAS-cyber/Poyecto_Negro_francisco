# Bubble Sort

Bubble Sort es un algoritmo de ordenamiento que funciona comparando elementos adyacentes y cambiándolos de lugar si están en el orden incorrecto. Su funcionamiento es repetitivo y simple, ya que recorre la lista varias veces, realizando intercambios hasta que la lista está completamente ordenada. 

## ¿Para qué es ideal?
Bubble Sort es ideal para listas pequeñas o cuando se requiere una implementación sencilla. Es útil para fines educativos y como introducción a los algoritmos de ordenamiento, pero no es recomendable para listas grandes o cuando se necesita un rendimiento óptimo, ya que existen algoritmos más eficientes como QuickSort o MergeSort.

## En qué se basa
El algoritmo se basa en la idea de comparar elementos adyacentes y realizar intercambios si están en el orden incorrecto. Este proceso se repite hasta que todos los elementos están en el orden correcto. A medida que el algoritmo avanza, los elementos más grandes "suben" hacia el final de la lista, como una burbuja ascendiendo.

## Funcionamiento del Algoritmo:
1. **Comparar** cada par de elementos adyacentes.
2. **Intercambiar** los elementos si están en el orden incorrecto (por ejemplo, si el primero es mayor que el segundo en un orden ascendente).
3. **Repetir** el proceso para cada par de elementos de la lista. Después de cada pasada, el siguiente mayor elemento se encuentra en su posición final.
4. El algoritmo se detiene cuando ya no se requieren intercambios, indicando que la lista está completamente ordenada.

 

## Características:
- **Estabilidad**: Es un algoritmo estable, lo que significa que no cambia el orden de los elementos con el mismo valor.
- **Facilidad de implementación**: Es muy fácil de implementar y entender.
- **Complejidad temporal**: O(n²) en el peor caso y en el promedio, lo que lo hace ineficiente para listas grandes.

Bubble Sort, análisis elaborado por: Hector Pat Sosa y Yasser Arturo Suarez Gonzalez
