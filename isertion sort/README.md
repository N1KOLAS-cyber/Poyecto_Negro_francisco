**Equipo:**

\- Luis Enrique Ramos Diaz

\- José Enrique Castañeda Náhuat

\- Esteban José Priego Moguel

\- Rodrigo González Tovar

**Insertion Sort**

El Ordenamiento por Inserción (Insertion Sort) es un algoritmo
fundamental en el estudio de estructuras de datos y algoritmos. Su
funcionamiento es intuitivo y fácil de comprender, lo que lo convierte
en una excelente introducción al concepto de ordenamiento. Su proceso
imita la manera en que una persona organizaría un mazo de cartas en la
mano: se toma cada carta y se inserta en la posición correcta dentro de
las ya ordenadas.

Este algoritmo opera dividiendo la lista en dos partes: una sección
ordenada y otra desordenada. Inicialmente, la sección ordenada comienza
con un solo elemento, pues un único elemento se considera, por
definición, ordenado. Luego, el algoritmo recorre la lista tomando un
elemento a la vez de la sección desordenada y lo compara con los que ya
han sido organizados, desplazando los mayores hacia la derecha hasta
encontrar la posición correcta para insertarlo.

Si bien Insertion Sort no es el método más eficiente para conjuntos de
datos grandes, ya que su complejidad en el peor caso es O(n²), resulta
especialmente útil cuando se trabaja con listas pequeñas o casi
ordenadas, donde su desempeño mejora significativamente. Además, es un
algoritmo estable, lo que significa que no altera el orden relativo de
elementos iguales, y es in-place, ya que no requiere estructuras de
datos adicionales para funcionar.

Su importancia radica no solo en su facilidad de implementación y
comprensión, sino también en que sienta las bases para algoritmos más
avanzados y es empleado en situaciones donde la eficiencia no es la
principal preocupación, sino la simplicidad y el bajo consumo de
memoria. Además, en ciertos escenarios, como la inserción de nuevos
elementos en listas parcialmente ordenadas, puede ser más eficiente que
otros métodos de ordenamiento más complejos.
