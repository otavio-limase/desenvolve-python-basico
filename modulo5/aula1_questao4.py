import datetime

agora = datetime.datetime.now()

dia = f"{agora.day:02}"
mes = f"{agora.month:02}"
ano = agora.year

hora = f"{agora.hour:02}"
minuto = f"{agora.minute:02}"

print(f"Data: {dia}/{mes}/{ano}")
print(f"Hora: {hora}:{minuto}")
