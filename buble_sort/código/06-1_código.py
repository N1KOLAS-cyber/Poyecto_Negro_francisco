import time
import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def best_case(n):
    return list(range(1, n+1))

def worst_case(n):
    return list(range(n, 0, -1))

def average_case(n):
    return np.random.permutation(n).tolist()

sizes = list(range(0, 10001, 1000))  # Modificado para tamaños desde 0 hasta 10,000
best_times = []
worst_times = []
average_times = []

for n in sizes:
    best_time = []
    for _ in range(20):  # 20 experimentos
        best_input = best_case(n)
        start = time.time()
        bubble_sort(best_input)
        end = time.time()
        best_time.append(end - start)
    best_times.append(np.mean(best_time))

    worst_time = []
    for _ in range(20):  # 20 experimentos
        worst_input = worst_case(n)
        start = time.time()
        bubble_sort(worst_input)
        end = time.time()
        worst_time.append(end - start)
    worst_times.append(np.mean(worst_time))

    avg_time = []
    for _ in range(20):  # 20 experimentos
        avg_input = average_case(n)
        start = time.time()
        bubble_sort(avg_input)
        end = time.time()
        avg_time.append(end - start)
    average_times.append(np.mean(avg_time))

# Gráficas de rendimiento
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_times, label="Best Case", color="green")
plt.plot(sizes, worst_times, label="Worst Case", color="red")
plt.plot(sizes, average_times, label="Average Case", color="blue")
plt.xlabel("Size of the Array (n)")
plt.ylabel("Execution Time (s)")
plt.legend()
plt.grid(True)
plt.show()