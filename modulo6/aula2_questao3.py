import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = sorted(set(lista1) & set(lista2))
contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao:", interseccao)
print("\nContagem:")

for item in interseccao:
    print(f"{item}: (lista1={contagem1[item]}, lista2={contagem2[item]})")
