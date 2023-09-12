# Lê o tamanho do vetor
N = int(input())

# Lê os elementos do vetor separados por espaço e os converte em uma lista de inteiros
X = list(map(int, input().split()))

# Encontra o menor valor e sua posição
menor_valor = min(X)
posicao = X.index(menor_valor)

# Imprime os resultados
print("Menor valor:", menor_valor)
print("Posicao:", posicao)
