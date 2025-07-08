N = int(input("Digite a qauntidade de experimentos: "))

total = 0
coelhos = 0
ratos = 0
sapos = 0
cont = 0

while cont < N:
    quant, tipo = input("Digite a qunatidade de cobaias e, separado por espaço, o tipo da cobaia: ").split()
    quant = int(quant)
    total += quant

    if ((tipo == "C") or (tipo =="c")):
        coelhos += quant
    elif ((tipo == "R") or (tipo =="r")):
        ratos += quant
    elif ((tipo == "S") or (tipo =="s")):
        sapos += quant

    cont += 1

percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
