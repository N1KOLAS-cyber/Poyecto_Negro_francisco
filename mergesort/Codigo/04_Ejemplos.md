\--Ejemplo 1: Mejor de los casos (Cuando el arreglo ya está ordenado y
cada división genera subarreglos equilibrados.)

Arreglo inicial: \[1, 2, 3, 4, 5, 6, 7, 8\]

Paso 1: División Dividimos el arreglo en dos mitades:

Mitad izquierda: \[1, 2, 3, 4\] Mitad derecha: \[5, 6, 7, 8\] División
recursiva de la mitad izquierda:

\[1, 2, 3, 4\] → \[1, 2\] y \[3, 4\] \[1, 2\] → \[1\] y \[2\] \[3, 4\] →
\[3\] y \[4\] División recursiva de la mitad derecha:

\[5, 6, 7, 8\] → \[5, 6\] y \[7, 8\] \[5, 6\] → \[5\] y \[6\] \[7, 8\] →
\[7\] y \[8\] Paso 2: Fusión Fusión de \[1\] y \[2\]: → \[1, 2\] Fusión
de \[3\] y \[4\]: → \[3, 4\] Fusión de \[1, 2\] y \[3, 4\]: → \[1, 2, 3,
4\] Fusión de \[5\] y \[6\]: → \[5, 6\] Fusión de \[7\] y \[8\]: → \[7,
8\] Fusión de \[5, 6\] y \[7, 8\]: → \[5, 6, 7, 8\] Fusión final de \[1,
2, 3, 4\] y \[5, 6, 7, 8\]: → \[1, 2, 3, 4, 5, 6, 7, 8\]

\--Ejemplo 2: Peor de los casos (Cuando el arreglo está completamente en
orden inverso, lo que genera el máximo número de comparaciones y
movimientos.)

Arreglo inicial: \[8, 7, 6, 5, 4, 3, 2, 1\]

Paso 1: División Dividimos el arreglo en dos mitades:

Mitad izquierda: \[8, 7, 6, 5\] Mitad derecha: \[4, 3, 2, 1\] División
recursiva de la mitad izquierda:

\[8, 7, 6, 5\] → \[8, 7\] y \[6, 5\] \[8, 7\] → \[8\] y \[7\] \[6, 5\] →
\[6\] y \[5\] División recursiva de la mitad derecha:

\[4, 3, 2, 1\] → \[4, 3\] y \[2, 1\] \[4, 3\] → \[4\] y \[3\] \[2, 1\] →
\[2\] y \[1\] Paso 2: Fusión Fusión de \[8\] y \[7\]: → \[7, 8\] Fusión
de \[6\] y \[5\]: → \[5, 6\] Fusión de \[7, 8\] y \[5, 6\]: → \[5, 6, 7,
8\] Fusión de \[4\] y \[3\]: → \[3, 4\] Fusión de \[2\] y \[1\]: → \[1,
2\] Fusión de \[3, 4\] y \[1, 2\]: → \[1, 2, 3, 4\] Fusión final de \[5,
6, 7, 8\] y \[1, 2, 3, 4\]: → \[1, 2, 3, 4, 5, 6, 7, 8\]
