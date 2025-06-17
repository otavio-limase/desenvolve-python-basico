# Lê a temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius
celsius = int((fahrenheit - 32) * (5 / 9))

# Imprime a mensagem formatada
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
