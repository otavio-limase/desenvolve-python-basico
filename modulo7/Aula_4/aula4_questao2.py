with open("frase.txt", "r", encoding="utf-8") as f:
    texto = f.read()

palavras = ''.join([c if c.isalpha() or c.isspace() else ' ' for c in texto]).split()

with open("palavras.txt", "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + '\n')

with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
