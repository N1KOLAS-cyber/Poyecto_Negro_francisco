## 📊 Análisis de Complejidad Temporal del Algoritmo Bubble Sort

El **algoritmo Bubble Sort** es conocido por ser sencillo pero ineficiente para listas grandes. A continuación, realizaremos un análisis de su complejidad temporal para los distintos casos: **Mejor Caso (Best Case)**, **Peor Caso (Worst Case)** y **Promedio (Average Case)**.

---

### Peor Caso (Worst Case):

**Parte algebraica:**

```
T(n) = C1(n) + C2(n(n-1)/2) + C3(n(n-1)/2) + C4(n(n-1)/2)
T(n) = O(n^2)
```

**Explicación:**
En el peor de los casos, la lista está ordenada de manera inversa, es decir, en orden descendente. Esto requiere el máximo número de comparaciones e intercambios. En cada pasada, el algoritmo realiza el número máximo de intercambios posibles.

**Ejemplo:** `A = [5, 4, 3, 2, 1]`

| Línea | Pseudocódigo                               | Costo                 | Tiempo             |
|-------|--------------------------------------------|-----------------------|--------------------|
| 1     | PARA i DESDE 0 HASTA n-1 HACER             | C1                    | n                  |
| 2     | PARA j DESDE 0 HASTA n-i-1 HACER           | C2                    | n(n-1)/2           |
| 3     | SI A[j] > A[j+1] ENTONCES                  | C3                    | n(n-1)/2           |
| 4     | intercambiar(A[j], A[j+1])                 | C4                    | n(n-1)/2           |

---

### Mejor Caso (Best Case):

**Parte algebraica:**

```
T(n) = C1(n) + C2(n-1) + C3(n-1)
T(n) = O(n)
```

**Explicación:**
En el mejor caso, la lista ya está ordenada. El algoritmo solo realiza una pasada sobre la lista, realizando una comparación por cada elemento. No se requieren intercambios, por lo que el algoritmo termina rápidamente.

**Ejemplo:** `A = [1, 2, 3, 4, 5]`

| Línea | Pseudocódigo                               | Costo                 | Tiempo             |
|-------|--------------------------------------------|-----------------------|--------------------|
| 1     | PARA i DESDE 0 HASTA n-1 HACER             | C1                    | n                  |
| 2     | PARA j DESDE 0 HASTA n-i-1 HACER           | C2                    | n-1                |
| 3     | SI A[j] > A[j+1] ENTONCES                  | C3                    | n-1                |
| 4     | intercambiar(A[j], A[j+1])                 | -                     | -                  |

---

### Caso Promedio (Average Case):

**Parte algebraica:**

```
T(n) = C1(n) + C2(n(n-1)/4) + C3(n(n-1)/4) + C4(n(n-1)/4)
T(n) = O(n^2)
```

**Explicación:**
En el caso promedio, la lista está desordenada aleatoriamente. El algoritmo realizará un número intermedio de comparaciones e intercambios. A pesar de la aleatoriedad, el algoritmo sigue siendo cuadrático en la mayoría de los casos debido a la necesidad de recorrer múltiples veces la lista.

**Ejemplo:** `A = [3, 1, 4, 5, 2, 8, 7, 6]`

| Línea | Pseudocódigo                               | Costo                 | Tiempo             |
|-------|--------------------------------------------|-----------------------|--------------------|
| 1     | PARA i DESDE 0 HASTA n-1 HACER             | C1                    | n                  |
| 2     | PARA j DESDE 0 HASTA n-i-1 HACER           | C2                    | n(n-1)/4           |
| 3     | SI A[j] > A[j+1] ENTONCES                  | C3                    | n(n-1)/4           |
| 4     | intercambiar(A[j], A[j+1])                 | C4                    | n(n-1)/4           |

---

### Resumen de Complejidad Temporal:

| Caso               | Complejidad Temporal |
|--------------------|----------------------|
| Mejor Caso         | `O(n)`              |
| Peor Caso          | `O(n^2)`            |
| Promedio (Caso Promedio) | `O(n^2)`      |



