n1 = float(input("Informe a nota N1: "))
n2 = float(input("Informe a nota N2: "))
n3 = float(input("Informe a nota N3: "))
media = (n1 + n2 + n3) / 3
if media >= 60:
    print("Aprovado")
elif media >= 40:
    print("Recuperção")
else:
    print("Reprovado")
print("Fim")
