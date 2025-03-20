//readme sobre ordenamiento sobre insercion
# Ordenamiento por Selección (Selection Sort)

## Descripción

El ordenamiento por selección es un algoritmo de ordenamiento que funciona seleccionando repetidamente el elemento mínimo (o máximo, dependiendo del orden deseado) de la parte no ordenada de la lista y colocándolo al principio (o al final) de la parte ordenada. El algoritmo divide la lista en dos partes: una sublista ya ordenada, que se construye de izquierda a derecha al inicio de la lista, y una sublista restante que aún no está ordenada.

## Funcionamiento

1.  **Encontrar el mínimo:** Se busca el elemento más pequeño en la sublista no ordenada.
2.  **Intercambiar:** Se intercambia el elemento mínimo encontrado con el primer elemento de la sublista no ordenada.
3.  **Repetir:** Se repiten los pasos 1 y 2 para la sublista restante, excluyendo los elementos ya ordenados.
4.  **Finalizar:** El proceso continúa hasta que toda la lista esté ordenada.

## Características

*   **Simple:** Es uno de los algoritmos de ordenamiento más sencillos de entender e implementar.
*   **Ineficiente para grandes listas:** Su complejidad temporal es de O(n^2), lo que lo hace ineficiente para listas grandes.
*   **Estable:** No es un algoritmo estable, ya que el orden relativo de elementos iguales puede cambiar.
*   **In-place:** Es un algoritmo "in-place", lo que significa que ordena la lista sin necesidad de memoria adicional significativa.

## Complejidad

*   **Mejor caso:** O(n^2)
*   **Peor caso:** O(n^2)
*   **Caso promedio:** O(n^2)

## Uso

El ordenamiento por selección es útil para:

*   **Listas pequeñas:** Cuando el tamaño de la lista es pequeño, su simplicidad puede ser más importante que su eficiencia.
*   **Fines educativos:** Es un buen algoritmo para aprender los conceptos básicos de ordenamiento.
*   **Situaciones donde la memoria es limitada:** Al ser un algoritmo "in-place", no requiere memoria adicional.
