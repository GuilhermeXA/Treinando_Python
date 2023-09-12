# Lê a quantidade de valores
N = int(input())

# Inicializa um dicionário para rastrear a contagem de cada número
contagem = {}

# Lê os valores e atualiza a contagem no dicionário
for _ in range(N):
    valor = int(input())
    if valor in contagem:
        contagem[valor] += 1
    else:
        contagem[valor] = 1

# Ordena as chaves do dicionário em ordem crescente
chaves_ordenadas = sorted(contagem.keys())

# Imprime a contagem de cada número
for chave in chaves_ordenadas:
    print(f'{chave} aparece {contagem[chave]} vez(es)')
