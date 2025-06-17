# aula2_questao4.py
# Validação de ficha de personagem para RPG.
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Digite os pontos de força (1‑20): "))
magia = int(input("Digite os pontos de magia (1‑20): "))

if classe == "guerreiro":
    consistente = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    consistente = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    consistente = (5 < forca <= 15) and (5 < magia <= 15)
else:
    consistente = False          # classe inválida

print(f"Pontos de atributo consistentes com a classe escolhida: {consistente}")
