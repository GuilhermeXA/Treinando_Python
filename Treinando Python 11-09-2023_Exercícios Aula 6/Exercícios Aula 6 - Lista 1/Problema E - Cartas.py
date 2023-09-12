# Lê as cinco cartas da sequência
cartas = list(map(int, input().split()))

# Verifica se as cartas estão ordenadas crescentemente
if cartas == sorted(cartas):
    print('C')
# Verifica se as cartas estão ordenadas decrescentemente
elif cartas == sorted(cartas, reverse=True):
    print('D')
# Caso contrário, não estão ordenadas
else:
    print('N')
