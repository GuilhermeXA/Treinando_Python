# Função para encontrar o menor número n possível
def encontrar_numero(A, B, C, D):
    for n in range(1, 1000001):  # Considerando um intervalo razoável para busca
        if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
            return n
    return -1

# Lendo os valores de A, B, C, e D
A, B, C, D = map(int, input().split())

# Chamando a função para encontrar o menor n possível
resultado = encontrar_numero(A, B, C, D)

# Imprimindo o resultado
print(resultado)
