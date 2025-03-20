## 📜 Pseudocódigo del Bubble Sort con su explicación:

```plaintext
ALGORITMO BubbleSort
ENTRADA: Una lista de n elementos
SALIDA: Lista ordenada

1. PARA i DESDE 0 HASTA n - 1 HACER
    - Se inicia un ciclo exterior que se repetirá n veces. Este ciclo controla el número de pasadas sobre la lista.
    
2.    intercambiado <- FALSO
    - Inicializamos la variable `intercambiado` como FALSO. Esta variable se usará para detectar si se ha realizado algún intercambio en esta pasada. Si no se realizan intercambios, significa que la lista ya está ordenada y podemos salir del ciclo.

3.    PARA j DESDE 0 HASTA n - i - 2 HACER
    - Este ciclo interior recorre la lista desde el primer elemento hasta el elemento que corresponde al último que aún necesita ser revisado en esta pasada.
    - `n - i - 2` asegura que no se revisen elementos ya ordenados en pasadas anteriores.

4.        SI lista[j] > lista[j + 1] ENTONCES
    - Comparamos el elemento actual con el siguiente. Si el elemento actual es mayor, significa que están en el orden incorrecto y necesitamos intercambiarlos.

5.            Intercambiar lista[j] y lista[j + 1]
    - Intercambiamos los elementos en la posición `j` y `j + 1` para que el mayor de los dos se mueva hacia el final de la lista.

6.            intercambiado <- VERDADERO
    - Actualizamos la variable `intercambiado` a VERDADERO para indicar que se realizó un intercambio en esta pasada.

7.    FIN PARA
    - Fin del ciclo interior. Se repite el proceso para el siguiente par de elementos.

8.    SI NO hubo intercambio ENTONCES
    - Si la variable `intercambiado` sigue siendo FALSO después de recorrer toda la lista, significa que no se han realizado intercambios, por lo que la lista ya está ordenada.

9.        SALIR DEL BUCLE
    - En este caso, terminamos el ciclo exterior antes de completar las n pasadas, ya que la lista está ordenada y no es necesario seguir recorriéndola.

10. FIN PARA
    - Fin del ciclo exterior.

DEVOLVER lista ordenada
- Finalmente, se devuelve la lista ordenada.
