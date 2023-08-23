# Lê o valor de N (número de comprimentos de varetas) da entrada
N = int(input())

# Enquanto N for diferente de 0 (condição de parada)
while N != 0:
    # Inicializa um dicionário para armazenar o número de varetas de cada comprimento
    varetas = {}

    # Lê os comprimentos e quantidades de varetas do conjunto
    for _ in range(N):
        C, V = map(int, input().split())
        varetas[C] = V

    # Calcula o máximo número de retângulos possíveis
    max_rectangles = min(varetas.values())

    # Imprime o resultado
    print(max_rectangles)

    # Lê o próximo valor de N para a próxima iteração
    N = int(input())
