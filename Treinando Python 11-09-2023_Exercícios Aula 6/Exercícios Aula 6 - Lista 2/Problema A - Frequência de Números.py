# Lê o número de valores
n = int(input())

# Inicializa um dicionário para contar a frequência de cada número
frequencia = {}

# Lê os valores e atualiza a frequência
for _ in range(n):
    valor = int(input())
    if valor in frequencia:
        frequencia[valor] += 1
    else:
        frequencia[valor] = 1

# Obtém os valores distintos em ordem crescente
valores_distintos = sorted(frequencia.keys())

# Imprime os valores distintos e suas frequências
for valor in valores_distintos:
    print(f'{valor} aparece {frequencia[valor]} vez(es)')
