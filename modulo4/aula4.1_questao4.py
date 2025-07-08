n = float(input("Insira a quantidade de elementos: "))
maior = 0
while n > 0:
    x = float(input("Insira o valor de X: "))
    if x > maior:
        maior = x
    n = n - 1
print(f"O maior elemento é: {maior}")
