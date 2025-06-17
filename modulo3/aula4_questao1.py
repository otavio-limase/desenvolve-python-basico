# aula4_questao1.py
# Lê dois números e informa se a soma é par ou ímpar.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
