def contar_diamantes(entrada):
    pilha = []
    diamantes = 0

    for char in entrada:
        if char == '<':
            pilha.append(char)
        elif char == '>' and pilha:
            pilha.pop()
            diamantes += 1

    return diamantes


N = int(input())

for _ in range(N):
    entrada = input()
    diamantes = contar_diamantes(entrada)
    print(diamantes)
