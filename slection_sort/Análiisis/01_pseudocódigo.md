Karlos , Darla , Angel, Ian
PROCEDIMIENTO selection_sort (Vector a [1:n])
    PARA I VARIANDO DE 1 HASTA n - 1 HACER
        ENCONTRAR [j] EL ELEMENTO MÁS PEQUEÑO DE [i + 1:n];
        INTERCAMBIAR [j] Y [i];

FIN PROCEDIMIENTO;

Primero, vas a buscar en toda la lista el número más pequeño.
Una vez que lo encuentras, lo tomas y lo pones al principio
de una nueva lista ordenada (o lo cambias de lugar
con el número que esté actualmente al principio
de tu lista original).

Luego, vas a buscar en el resto de la lista
(sin contar el número que ya pusiste al principio)
el siguiente número más pequeño. Lo tomas y lo pones
justo después del primer número en tu lista ordenada
(o lo cambias de lugar con el número que esté
en esa segunda posición de tu lista original).

Vas a repetir este proceso. En cada paso, vas a encontrar
el número más pequeño que queda en la parte desordenada
de la lista y lo vas a colocar en la siguiente posición
disponible en la parte ordenada.

Continuarás haciendo esto hasta que no queden más números
desordenados. En ese momento, toda tu lista estará
ordenada de menor a mayor.

Básicamente, en cada paso, seleccionas el elemento
más pequeño que falta y lo colocas en su lugar correcto.
Por eso se llama "ordenamiento por selección" 

## Explicación Detallada

El algoritmo de ordenamiento por selección funciona de la siguiente manera:

> Primero, se busca en toda la lista el número más pequeño. Una vez que se encuentra, se toma y se pone al principio de una nueva lista ordenada (o se cambia de lugar con el número que esté actualmente al principio de la lista original).

> Luego, se busca en el resto de la lista (sin contar el número que ya se puso al principio) el siguiente número más pequeño. Se toma y se pone justo después del primer número en la lista ordenada (o se cambia de lugar con el número que esté en esa segunda posición de la lista original).

> Se repite este proceso. En cada paso, se encuentra el número más pequeño que queda en la parte desordenada de la lista y se coloca en la siguiente posición disponible en la parte ordenada.

Se continúa haciendo esto hasta que no queden más números desordenados. En ese momento, toda la lista estará ordenada de menor a mayor.

Básicamente, en cada paso, se **selecciona** el elemento más pequeño que falta y se coloca en su lugar correcto. Por eso se llama "**ordenamiento por selección**".

## Ejemplo Paso a Paso


EJEMPLO 1
[Inicio]
↓
[Mostrar lista inicial: [7, 2, 6, 4]]
↓
[Para i desde 0 hasta 2]
↓
[Encontrar el índice del elemento más pequeño en [i:3]]
↓
[i = 0: El mínimo es 2 en el índice 1]
↓
[Intercambiar lista[0] y lista[1]: [2, 7, 6, 4]]
↓
[Mostrar paso actual: [2, 7, 6, 4]]
↓
[¿i == 2?] → No
↓
[Volver al Bucle Principal]
↓
[i = 1: El mínimo es 4 en el índice 3]
↓
[Intercambiar lista[1] y lista[3]: [2, 4, 6, 7]]
↓
[Mostrar paso actual: [2, 4, 6, 7]]
↓
[¿i == 2?] → No
↓
[Volver al Bucle Principal]
↓
[i = 2: El mínimo es 6 en el índice 2]
↓
[Intercambiar lista[2] y lista[2]: [2, 4, 6, 7]]
↓
[Mostrar paso actual: [2, 4, 6, 7]]
↓
[¿i == 2?] → Sí → [Mostrar lista ordenada: [2, 4, 6, 7]]
↓                       ↓
No                      [Fin]
↓
[Volver al Bucle Principal]