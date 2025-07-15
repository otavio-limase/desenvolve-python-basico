from collections import Counter

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ").lower()

palavras = frase.split()
anagramas = [p for p in palavras if Counter(p.lower()) == Counter(objetivo)]
print("Anagramas:", anagramas)
