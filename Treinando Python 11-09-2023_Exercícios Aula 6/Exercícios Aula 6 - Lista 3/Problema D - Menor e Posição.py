# Leia o valor N
N = int(input())

# Leia os valores do vetor X
X = list(map(int, input().split()))

# Encontre o menor elemento do vetor e sua posição
menor_valor = min(X)
posicao = X.index(menor_valor)

# Mostre o menor valor e sua posição
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
