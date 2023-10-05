def encontra_sabre_de_luz(terreno):
    for i in range(1, len(terreno) - 1):
        for j in range(1, len(terreno[0]) - 1):
            if (
                terreno[i][j] == 42
                and terreno[i - 1][j] == terreno[i + 1][j] == terreno[i][j - 1] == terreno[i][j + 1] == 7
            ):
                return i + 1, j + 1
    return 0, 0

# Leitura da entrada
N, M = map(int, input().split())
terreno = [list(map(int, input().split())) for _ in range(N)]

# Procura pelo padrão do sabre de luz
x, y = encontra_sabre_de_luz(terreno)

# Saída
print(f"{x} {y}")
