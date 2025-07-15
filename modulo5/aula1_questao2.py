import random
import math

n = int(input("Digite a quantidade de números a serem gerados: "))

soma = 0
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz = math.sqrt(soma)

print(f"A raiz quadrada da soma dos {n} valores é: {round(raiz, 2)}")
