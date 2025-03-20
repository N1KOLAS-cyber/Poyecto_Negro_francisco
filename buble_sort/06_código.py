import time
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing

def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break

def best_case(n):
    return np.arange(1, n + 1).tolist()

def worst_case(n):
    return np.arange(n, 0, -1).tolist()

def average_case(n):
    return np.random.permutation(n).tolist()

def measure_time(case_func, n, iterations):
    times = []
    for _ in range(iterations):
        arr = case_func(n)
        start = time.perf_counter()
        bubble_sort(arr)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times)

def run_experiment():
    sizes = np.arange(0, 10001, 1000)
    iterations = 20

    with multiprocessing.Pool() as pool:
        best_times = pool.starmap(measure_time, [(best_case, n, iterations) for n in sizes])
        worst_times = pool.starmap(measure_time, [(worst_case, n, iterations) for n in sizes])
        average_times = pool.starmap(measure_time, [(average_case, n, iterations) for n in sizes])

    # Gráfica optimizada
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, best_times, label="Best Case (Ordenado)", color="green")
    plt.plot(sizes, worst_times, label="Worst Case (Invertido)", color="red")
    plt.plot(sizes, average_times, label="Average Case (Aleatorio)", color="blue")

    plt.xlabel("Tamaño del Arreglo (n)")
    plt.ylabel("Tiempo de Ejecución (s)")
    plt.title("Rendimiento del Bubble Sort en Diferentes Escenarios")

    plt.yscale("log")  # Escala logarítmica para visualizar mejor las diferencias
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    plt.savefig("bubble_sort_performance.png")  # Guarda la gráfica
    plt.show()

if __name__ == "__main__":
    run_experiment()