import random

def encrypt(lista):
    chave = random.randint(1, 10)
    criptografados = []
    for nome in lista:
        cript = ''.join([chr(((ord(c)-33 + chave) % 94) + 33) for c in nome])
        criptografados.append(cript)
    return criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
cript, chave = encrypt(nomes)
print("Chave:", chave)
print("Nomes criptografados:", cript)
