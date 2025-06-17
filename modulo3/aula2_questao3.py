# aula2_questao3.py
# Admissão no clube juvenil de jogos de tabuleiro.
idade = int(input("Digite sua idade: "))
jogou_3_plus = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False) ").strip().lower() == "true"
vitorias = int(input("Quantos jogos já venceu? "))
apto = (16 <= idade <= 18) and jogou_3_plus and (vitorias >= 1)
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
