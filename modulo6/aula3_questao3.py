import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)
max_inicio = max_fim = i = 0
while i < len(lista):
    if lista[i] < 0:
        inicio = i
        while i < len(lista) and lista[i] < 0:
            i += 1
        fim = i
        if (fim - inicio) > (max_fim - max_inicio):
            max_inicio, max_fim = inicio, fim
    else:
        i += 1

del lista[max_inicio:max_fim]

print("Lista após remoção do intervalo negativo:", lista)
