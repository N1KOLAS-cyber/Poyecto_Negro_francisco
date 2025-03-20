Complejidad computacional y análisis de casos 

El análisis de la complejidad computacional de QuickSort se basa en cómo se comporta el algoritmo dependiendo de los diferentes escenarios que pueden presentarse al ordenar una lista y el elemento que se tome como pivote (como se describió en los dos ejemplos anteriores), lo cual lo hace más complejo de analizar en tres casos principales: **el caso promedio**, **el peor caso** y **el mejor caso**.  

**1. Caso Promedio** 

En el caso promedio, se asume que el pivote es la media según su índice, lo que permite dividir la lista de manera equilibrada en cada paso del algoritmo. 

- **División de la lista**: A medida que el algoritmo avanza, la lista se divide aproximadamente a la mitad en cada paso. En cada partición, el tiempo de ejecución para ordenar los subarreglos es proporcional al tamaño de esos subarreglos. 
- **Recursión**: En cada nivel recursivo, QuickSort realiza dos llamadas recursivas (una para la sublista de los elementos menores y otra para la sublista de los elementos mayores). Esto significa que el número total de comparaciones realizadas es proporcional a la altura de la recursión. 

La **complejidad computacional promedio** de QuickSort es: 

- **Tiempo de ejecución**: O(n log n)  
- **n** es el número de elementos de la lista. 
- **log n** representa el número de veces que la lista se divide a la mitad durante el proceso. 

El caso promedio es el más eficiente de todos y es el que se espera en la mayoría de las situaciones al aplicar QuickSort a una lista no ordenada. 

**2. Peor Caso** 

El peor caso ocurre cuando el pivote elegido no divide bien la lista. Esto puede suceder si siempre se escoge un pivote muy desfavorable, como el primer o el último elemento en una lista ya ordenada o inversamente ordenada. En este caso, el algoritmo no divide la lista de manera equilibrada, y uno de los subarreglos resultantes será mucho más grande que el otro. 

- **División desequilibrada**: En este escenario, en cada paso recursivo el algoritmo solo reduce el tamaño de la lista en un solo elemento, lo que resulta en una recursión de **n niveles**. 
- **Tiempo de ejecución**: Si el pivote es el peor en cada caso (por ejemplo, el primer o el último elemento de la lista), el tiempo de ejecución es: 
- **O(n²)**: El algoritmo tiene que recorrer todos los elementos en cada nivel de recursión. 

Este comportamiento se observa generalmente cuando QuickSort recibe una lista ya ordenada o casi ordenada, lo cual puede ocurrir si el pivote elegido es inadecuado para esas listas. 

**3. Mejor Caso** 

El mejor caso ocurre cuando el pivote elegido divide la lista de manera equilibrada en cada paso de la recursión, esto sucede con mayor afinidad al considerar el pivote como la media de la lista. Esto significa que, en cada nivel de recursión, la lista se divide casi a la mitad. 

- **División equilibrada**: Si el pivote divide la lista de manera eficiente, QuickSort puede ordenar los elementos en aproximadamente logaritmos de los niveles de recursión. 
- **Tiempo de ejecución**: En este caso, el tiempo de ejecución es óptimo: 
- **O(n log n)**: Cada nivel recursivo realiza un número de comparaciones lineales, y el número total de niveles de recursión es logarítmico. 

Este caso es más probable cuando el pivote se selecciona de manera adecuada (por ejemplo, el pivote en el medio de la lista o un pivote aleatorio). 

**4. Análisis:** 

Las llamadas recursivas siguen la siguiente forma para el mejor de los casos:  

T(n)=2T(n/2)+O(n)

Que termina con la siguiente forma: 

T(n)=O(nlog(n)) 

Las llamadas recursivas siguen la siguiente forma para el peor de los casos: 

T(n)=T(n-1)+O(n)

Que termina con la siguiente forma: 

T(n)=O(n^2)

Las llamadas recursivas siguen la siguiente forma para el caso promedio:  

T(n)=2T(n/2)+O(n)

Que termina con la siguiente forma: 

T(n)=O(n log(n))

**Comparando los tres casos:** 

|**Caso** |**Número de comparaciones** |**Complejidad** |
| :- | :- | :- |
|Mejor Caso |O(n log n) |Eficiencia alta |
|Caso Promedio |O(n log n) |Eficiencia promedio |
|Peor Caso |O(n²) |Eficiencia baja |



El algoritmo es muy eficiente en el caso promedio, ya que generalmente realiza una cantidad de comparaciones proporcional a O(n log n). Sin embargo, en el peor caso, puede volverse muy ineficiente con un tiempo de ejecución de O(n²). 

**5. Factores que afectan la complejidad de QuickSort** 

La complejidad de QuickSort también depende de varios factores: 

- **Elección del pivote**: Como se ha mencionado, elegir un buen pivote es crucial para el rendimiento de QuickSort. En general, se pueden usar estrategias como: 
- Elegir el primer o último elemento como pivote (puede ser ineficiente en listas ya ordenadas o casi ordenadas). 
- Elegir el pivote aleatorio o el pivote en el medio (puede mejorar el rendimiento en la mayoría de los casos). 
- **Tamaño de la lista**: El tamaño de la lista también influye en el número de recursiones necesarias. Aunque QuickSort puede funcionar muy bien en listas grandes debido a su complejidad O(n log n), en listas pequeñas, puede no ser tan eficiente como otros algoritmos como **Insertion Sort**. 
- **Optimización**: En implementaciones prácticas de QuickSort, a menudo se realiza una optimización cuando el tamaño de las sublistas es pequeño, utilizando un algoritmo diferente (por ejemplo, Insertion Sort) en lugar de seguir con QuickSort para evitar el sobrecosto de la recursión. 

Para facilitar el análisis  práctico se considerará de manera arbitraria la asignación del pivote como la media según el índice la lista y las sublistas subsecuentes con el fin de describir su complejidad computacional, sin embargo, es importante resaltar que es con fines académicos ya que los resultados obtenidos no se podrían generalizar ya que actualmente existen incluso formas más eficientes de aplicar el algoritmo Quicksort, es decir, nos estaríamos ubicando en el conocimiento y entendimiento del funcionamiento algorítmico más allá de querer encontrar la forma más eficiente de aplicar, dejando este último como una propuesta para futuros análisis con un enfoque diferente. 

Tabla de complejidad de los distintos casos y de diferentes tamaños de entrada cuando el pivote es el primer elemento 

|**Tamaño de entrada (n)**|**Mejor caso O (n log n) (Pivote primero)**|**Caso promedio O (n log n) (Pivote primero)**|**Peor caso O(n^2) (Pivote primero)**|
| :-: | :-: | :-: | :-: |
|**10**|33|39|100|
|**50**|282|338|2500|
|**100**|664|797|10000|
|**500**|4482|5379|250000|
|**1000**|9965|11958|1000000|
|**5000**|61438|73726|25000000|
|**10000**|132877|159452|100000000|
|**20000**|285754|342905|400000000|
|**50000**|780482|936578|2500000000|
|**100000**|1660964|1993156|10000000000|


Tabla de complejidad de los distintos casos y de diferentes tamaños de entrada cuando el pivote es el elemento medio. 

|**Tamaño de entrada (n)**|**Mejor caso O (n log n) (Pivote medio)**|**Caso promedio O (n log n) (Pivote medio)**|**Peor caso O(n log n) (Pivote medio)**|
| :-: | :-: | :-: | :-: |
|**10**|33|33|43|
|**50**|282|282|366|
|**100**|664|664|863|
|**500**|4482|4482|5827|
|**1000**|9965|9965|12955|
|**5000**|61438|61438|79870|
|**10000**|132877|132877|172740|
|**20000**|285754|285754|371480|
|**50000**|780482|780482|1014626|
|**100000**|1660964|1660964|2159253|
