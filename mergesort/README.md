# 🔍 Investigación sobre Merge Sort

**📌 Realizado por el equipo:**

- **Jorge Emmanuel Ruiz Castilla**
- **Nicolás Abraham Gamboa Novelo**
- **Lilia Yire Contreras García**
- **Juan Esteban Pérez Velázquez**

## 📖 Definición

El algoritmo **Merge Sort** es un método de ordenamiento que **divide una lista en partes, las ordena y luego las fusiona de manera ordenada**. Es un **algoritmo recursivo** basado en la técnica de **"divide y vencerás"**.

🔹 Características

✅ Es un algoritmo **eficiente y general** para ordenar listas o arrays.
✅ Es un **ejemplo clásico** de la estrategia "divide y vencerás".
✅ Tiene una **complejidad de O(n log n)** en todos los casos.
✅ **Fácilmente paralelizable**, lo que permite distribuir la carga en múltiples procesadores.
✅ Ventajas

🔹 **Eficiencia garantizada:** Su complejidad en el mejor, peor y caso promedio es **O(n log n)**, lo que lo hace más predecible que otros algoritmos como QuickSort.

🔹 **Ordenamiento estable:** Mantiene el **orden relativo de elementos con el mismo valor**, lo que es útil en bases de datos y aplicaciones donde se requiere estabilidad.

🔹 **Adecuado para listas enlazadas:** Funciona bien con **listas enlazadas**, ya que no requiere acceso aleatorio a los elementos, a diferencia de QuickSort.

🔹 **Ideal para grandes volúmenes de datos:** Se usa en sistemas con **acceso secuencial a datos**, como bases de datos o archivos de gran tamaño.

🔹 **Fácilmente paralelizable:** Su estrategia de "divide y vencerás" permite dividir el trabajo y ejecutarlo en **múltiples procesadores**.

## ❌ Desventajas

🔸 **Mayor uso de memoria:** Requiere **espacio adicional O(n)**, lo que puede ser un problema en sistemas con **memoria limitada**.

🔸 **Más lento que QuickSort en la práctica:** Aunque su peor caso es mejor que QuickSort, en la mayoría de los casos este último es más rápido debido a **una mejor localización en memoria**.

🔸 **No es in-place:** Necesita **estructuras adicionales** para combinar los subarreglos, a diferencia de QuickSort, que puede realizarse en el mismo arreglo.

🔸 **Mayor número de movimientos de datos:** Realiza más operaciones de **lectura y escritura**, lo que puede ser costoso en sistemas con discos duros.

**📌 ¿Cuándo usar Merge Sort?**

✅ Cuando se necesita un **ordenamiento estable**.
✅ Si trabajas con **listas enlazadas**.
✅ Cuando los datos son **demasiado grandes para caber en memoria** y deben ordenarse en almacenamiento externo.
✅ Si quieres aprovechar la **paralelización**.

## 🏆 Creador

El algoritmo **Merge Sort** fue desarrollado por **John von Neumann en 1945**.
