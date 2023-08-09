# Ler o valor inteiro representando o tempo em segundos
tempo_total_segundos = int(input())

# Calculando horas, minutos e segundos
horas = tempo_total_segundos // 3600
tempo_total_segundos %= 3600
minutos = tempo_total_segundos // 60
segundos = tempo_total_segundos % 60

# Imprimir o tempo no formato desejado
print(f"{horas}:{minutos}:{segundos}")
