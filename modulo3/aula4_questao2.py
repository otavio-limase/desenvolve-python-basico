# aula4_questao2.py
# Classificação de filmes por avaliação (1–5).
nota = int(input("Digite a avaliação do filme (1 a 5): "))

if nota == 5:
    print("Excelente!")
elif nota == 4:
    print("Muito Bom!")
elif nota == 3:
    print("Bom!")
elif nota == 2:
    print("Regular.")
elif nota == 1:
    print("Ruim.")
else:
    print("Valor inválido – digite de 1 a 5.")
