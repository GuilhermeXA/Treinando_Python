from itertools import product

def soma_conjuntos_mais_caros(P, M, F, Q, B, K):
    tipos_livros = [P, M, F, Q, B]
    valores_livros = []

    for _ in tipos_livros:
        valores_livros.append(list(map(int, input().split())))

    conjuntos_distintos = set(product(*valores_livros))
    conjuntos_distintos = sorted(conjuntos_distintos, key=lambda conjunto: sum(conjunto), reverse=True)

    total = sum(sum(conjunto) for conjunto in conjuntos_distintos[:K])
    return total

# Leitura da entrada
P = int(input())
M = int(input())
F = int(input())
Q = int(input())
B = int(input())
K = int(input())

# Chamada da função e impressão do resultado
resultado = soma_conjuntos_mais_caros(P, M, F, Q, B, K)
print(resultado)
