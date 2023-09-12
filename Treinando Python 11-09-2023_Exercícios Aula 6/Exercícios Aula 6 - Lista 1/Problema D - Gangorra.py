# Lê os pesos e comprimentos da gangorra
P1, C1, P2, C2 = map(int, input().split())

# Calcula o momento das crianças em ambos os lados
momento_esquerda = P1 * C1
momento_direita = P2 * C2

# Verifica o equilíbrio da gangorra e imprime o resultado
if momento_esquerda == momento_direita:
    print('0')
elif momento_esquerda < momento_direita:
    print('1')
else:
    print('-1')
