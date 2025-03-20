import time

def bubble_sort(arr):
    print(f"\nLista inicial: {arr}")
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Si no hubo intercambios, el arreglo ya está ordenado
        print(f"Paso {i + 1}: {arr}")  # Mostrar el estado de la lista después de cada pasada
         
    return arr

# Ejemplo 1: Worst Case
print("Ejemplo 1: Worst Case")
resultado1 = bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(f"Lista ordenada: {resultado1}")

# Ejemplo 2: Average Case
print("\nEjemplo 2: Average Case")
resultado2 = bubble_sort([3, 1, 4, 5, 2, 8, 7, 6, 10, 9])
print(f"Lista ordenada: {resultado2}")

# Ejemplo 3: Best Case
print("\nEjemplo 3: Best Case")
resultado3 = bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Lista ordenada: {resultado3}")