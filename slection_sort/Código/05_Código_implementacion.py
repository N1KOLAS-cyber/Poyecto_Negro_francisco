#Karlos , Darla , Angel, Ian
import time
import matplotlib.pyplot as plt
import random

# Ordenamiento por selección
def ordenamiento_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        índice_mínimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[índice_mínimo]:
                índice_mínimo = j
        # Intercambiar el mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[índice_mínimo] = lista[índice_mínimo], lista[i]

# Función para medir el tiempo de ejecución del ordenamiento
def medir_tiempo(A):
    inicio = time.perf_counter()  # Mayor precisión que time.time()
    ordenamiento_por_seleccion(A)  # Ordenar la lista
    fin = time.perf_counter()
    return fin - inicio  # Tiempo en segundos

# Tamaños de las listas a probar
tamaños = list(range(0, 1000, 100))  # Desde 10 hasta 500 en intervalos de 10
tiempos_mejor = []
tiempos_peor = []
tiempos_promedio = [] 

# Número de pruebas para cada tamaño de lista
num_pruebas = 20

for n in tamaños:
    tiempos_mejor_local = []
    tiempos_peor_local = []
    tiempos_promedio_local = []

    for _ in range(num_pruebas):
        # Mejor caso: la lista ya está ordenada
        A_mejor = list(range(n))
        tiempos_mejor_local.append(medir_tiempo(A_mejor))

        # Peor caso: la lista está ordenada en orden inverso
        A_peor = list(range(n, 0, -1))  # Lista en orden inverso
        tiempos_peor_local.append(medir_tiempo(A_peor))

        # Caso promedio: lista aleatoria
        A_promedio = random.sample(range(n), n)  # Lista aleatoria
        tiempos_promedio_local.append(medir_tiempo(A_promedio))

    # Se toman los valores promedio de cada caso
    tiempos_mejor.append(sum(tiempos_mejor_local) / len(tiempos_mejor_local))
    tiempos_peor.append(sum(tiempos_peor_local) / len(tiempos_peor_local))
    tiempos_promedio.append(sum(tiempos_promedio_local) / len(tiempos_promedio_local))

# Graficar los resultados
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
plt.plot(tamaños, tiempos_mejor, color='blue', linestyle='-', linewidth=2, label='Mejor caso (ordenada)')
plt.plot(tamaños, tiempos_peor, color='red', linestyle='-', linewidth=2, label='Peor caso (inversa)')
plt.plot(tamaños, tiempos_promedio, color='green', linestyle='-', linewidth=2, label='Caso promedio (aleatoria)')

# Etiquetas y título
plt.xlabel("Tamaño del Arreglo (n)", fontsize=12)
plt.ylabel("Tiempo de ejecución (s)", fontsize=12)
plt.title("Tiempos de Ejecución del Ordenamiento por Selección", fontsize=14)
plt.legend()
plt.grid(True)  # Agregar cuadrícula

# Mostrar gráfica
plt.show()