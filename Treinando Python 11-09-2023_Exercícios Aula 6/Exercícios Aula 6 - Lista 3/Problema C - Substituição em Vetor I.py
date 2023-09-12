# Crie um vetor X com 10 elementos
X = []

# Leia os 10 valores inteiros e insira no vetor X
for i in range(10):
    valor = int(input())
    X.append(valor)

# Substitua os valores nulos e negativos por 1
for i in range(10):
    if X[i] <= 0:
        X[i] = 1

# Mostre o vetor X
for i in range(10):
    print(f"X[{i}] = {X[i]}")
