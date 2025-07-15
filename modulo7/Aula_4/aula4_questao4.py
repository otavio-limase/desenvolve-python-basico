import random
import os

# === Criação dos arquivos, caso não existam ===
if not os.path.exists("gabarito_forca.txt"):
    palavras = [
        "computador",
        "python",
        "engenharia",
        "desenvolvimento",
        "programa",
        "rede",
        "algoritmo",
        "matematica",
        "sistema",
        "logica"
    ]

    with open("gabarito_forca.txt", "w", encoding="utf-8") as f:
        for palavra in palavras:
            f.write(palavra + "\n")

if not os.path.exists("gabarito_enforcado.txt"):
    estagios = [
        "  |---|\n      |\n      |\n      |\n=========",
        "  |---|\n  O   |\n      |\n      |\n=========",
        "  |---|\n  O   |\n  |   |\n      |\n=========",
        "  |---|\n  O   |\n /|   |\n      |\n=========",
        "  |---|\n  O   |\n /|\\  |\n      |\n=========",
        "  |---|\n  O   |\n /|\\  |\n /    |\n=========",
        "  |---|\n  O   |\n /|\\  |\n / \\  |\n========="
    ]

    with open("gabarito_enforcado.txt", "w", encoding="utf-8") as f:
        for estagio in estagios:
            f.write(estagio + "\n\n")

# === Função que imprime o estágio do enforcado ===
def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        estagios = f.read().strip().split("\n\n")
    print(estagios[erros])

# === Leitura da lista de palavras ===
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f.readlines()]

# Escolhe uma palavra aleatória
palavra = random.choice(palavras)
visivel = ["_" for _ in palavra]
tentativas = []
erros = 0

print("Jogo da Forca!")

# === Loop principal do jogo ===
while erros < 6 and "_" in visivel:
    print("\nPalavra:", ' '.join(visivel))
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in tentativas:
        print("Você já tentou essa letra.")
        continue

    tentativas.append(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                visivel[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

# === Fim do jogo ===
if "_" not in visivel:
    print("\nParabéns! Você acertou:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)
