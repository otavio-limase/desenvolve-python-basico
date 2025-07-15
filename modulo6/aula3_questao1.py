numeros = []
print("Digite pelo menos 4 números inteiros (digite 'ok' para encerrar):")

while True:
    entrada = input()
    if entrada.lower() == "ok":
        if len(numeros) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números.")
            continue
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Digite um número inteiro ou 'ok' para encerrar.")

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
