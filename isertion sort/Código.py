import time

def insertion_sort(arr):
    print(f"\nLista inicial: {arr}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Paso {i}: {arr}")  # Mostrar cada cambio en la lista
        time.sleep(1)  # Pausa para visualizar mejor los pasos
    return arr

# Ejemplo 1
resultado1 = insertion_sort([7, 2, 6, 4])
print(f"Lista ordenada: {resultado1}")

# Ejemplo 2
resultado2 = insertion_sort([5, 2, 4, 6, 1, 3])
print(f"Lista ordenada: {resultado2}")
