# aula4_questao3.py
# Verificador de ano bissexto.
ano = int(input("Digite um ano: "))

bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

print("Bissexto" if bissexto else "Não Bissexto")

# --- testes sugeridos ---
# 1900 → Não Bissexto
# 2000 → Bissexto
# 2016 → Bissexto
# 2017 → Não Bissexto
