# Lê o valor em reais
valor = int(input())

# Lista de notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada tipo de nota, calcula a quantidade e imprime
for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R${nota},00")
    valor = valor % nota
