# aula4_questao4.py
# Calculadora de frete para entrega expressa.
distancia = float(input("Distância da entrega (km): "))
peso = float(input("Peso do pacote (kg): "))

# Tarifa por kg de acordo com a faixa de distância
if distancia <= 100:
    tarifa = 1.0
elif distancia <= 300:
    tarifa = 1.5
else:
    tarifa = 2.0

valor_frete = tarifa * peso

# Taxa extra se peso > 10 kg
if peso > 10:
    valor_frete += 10.0

print(f"Valor do frete: R${valor_frete:.2f}")
