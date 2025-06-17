# aula2_questao5.py
# Verificador de aposentadoria.
genero = input("Digite seu gênero (M/F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

regra_idade = (genero == "F" and idade > 60) or (genero == "M" and idade >= 65)
regra_tempo = tempo_servico >= 30
regra_mista = (idade >= 60) and (tempo_servico >= 25)

aposenta = regra_idade or regra_tempo or regra_mista
print(f"Pode se aposentar: {aposenta}")
