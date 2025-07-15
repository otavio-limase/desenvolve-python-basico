import random

lista = [random.randint(-100, 100) for _ in range(20)]
lista_ordenada = sorted(lista)
indice_max = lista.index(max(lista))
indice_min = lista.index(min(lista))

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_max)
print("Índice do menor valor:", indice_min)
