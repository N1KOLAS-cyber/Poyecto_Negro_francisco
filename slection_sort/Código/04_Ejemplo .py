
def ordenamiento_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        índice_mínimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[índice_mínimo]:
                índice_mínimo = j
        # Intercambiar el mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[índice_mínimo] = lista[índice_mínimo], lista[i]

#ejemplos de uso paso a paso
lista_ejemplo = [64, 25, 12, 22, 11]
print("Lista original:", lista_ejemplo)
ordenamiento_por_seleccion(lista_ejemplo)
print("Lista ordenada:", lista_ejemplo)

lista_ejemplo2 = [5, 4, 3, 2, 1]
print("Lista original:", lista_ejemplo2)
ordenamiento_por_seleccion(lista_ejemplo2)
print("Lista ordenada:", lista_ejemplo2)

lista_ejemplo3 = [1, 2, 3, 4, 5]
print("Lista original:", lista_ejemplo3)
ordenamiento_por_seleccion(lista_ejemplo3)
print("Lista ordenada:", lista_ejemplo3)
