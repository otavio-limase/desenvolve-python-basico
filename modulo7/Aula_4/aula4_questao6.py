resultado = {}
with open("C:/Users/PDITA000/OneDrive/Área de Trabalho/desenvolve-python-basico/modulo7/Aula_4/spotify-2023.csv", "r", encoding="latin-1") as f:
    next(f)  # pula o cabeçalho
    for linha in f:
        if linha.count('"') >= 2:
            continue  # ignora campos com aspas que atrapalham o split
        partes = linha.strip().split(",")
        if len(partes) < 9:
            continue

        try:
            nome = partes[0]
            artista = partes[1]
            ano = int(partes[3])
            streams = int(partes[8])
        except:
            continue

        if 2012 <= ano <= 2022:
            if (ano not in resultado) or (streams > resultado[ano][3]):
                resultado[ano] = [nome, artista, ano, streams]

lista_resultado = [resultado[ano] for ano in sorted(resultado)]
print(lista_resultado)
