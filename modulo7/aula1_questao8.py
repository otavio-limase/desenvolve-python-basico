def calcula_digito(cpf_base, multiplicadores):
    soma = sum([int(digito) * mult for digito, mult in zip(cpf_base, multiplicadores)])
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace(".", "").replace("-", "")
base = cpf[:9]

dig1 = calcula_digito(base, range(10, 1, -1))
dig2 = calcula_digito(base + dig1, range(11, 1, -1))

if cpf[-2:] == dig1 + dig2:
    print("Válido")
else:
    print("Inválido")
