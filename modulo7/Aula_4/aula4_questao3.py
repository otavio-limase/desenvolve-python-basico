nonato_count = 0
iria_count = 0
maior_linha = ""
with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

print("Primeiras 25 linhas:")
print(''.join(linhas[:25]))

print("Total de linhas:", len(linhas))

for linha in linhas:
    if len(linha) > len(maior_linha):
        maior_linha = linha
    palavras = linha.lower().split()
    nonato_count += palavras.count("nonato")
    iria_count += [p for p in palavras if p == "íria" or p == "iria"].count("íria")

print("Linha com mais caracteres:", maior_linha.strip())
print("Menções a 'Nonato':", nonato_count)
print("Menções a 'Íria':", iria_count)
