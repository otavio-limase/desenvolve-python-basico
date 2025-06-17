# Lê o comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Lê a largura do terreno
largura = int(input("Digite a largura do terreno (em metros): "))

# Lê o preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (em reais): "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = area_m2 * preco_m2

# Imprime o resultado com duas casas decimais
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
