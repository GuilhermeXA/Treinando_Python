def encontrar_ponto_divisao(territorio):
    total = sum(territorio)
    soma_esquerda = 0

    for i in range(len(territorio)):
        total -= territorio[i]
        if soma_esquerda == total:
            return i + 1  # Adicionando 1 porque os índices começam em 1 no problema
        soma_esquerda += territorio[i]

# Leitura da entrada
N = int(input())
territorio = list(map(int, input().split()))

# Encontrar o ponto de divisão
ponto_divisao = encontrar_ponto_divisao(territorio)

# Saída
print(ponto_divisao)
