# Lê o número de bandejas
N = int(input())

# Inicializa a variável para armazenar o total de copos quebrados
total_copos_quebrados = 0

# Loop para ler cada bandeja
for _ in range(N):
    # Lê o número de latas e copos na bandeja
    L, C = map(int, input().split())

    # Verifica se há mais latas do que copos, e se sim, incrementa o total de copos quebrados
    if L > C:
        total_copos_quebrados += C

# Imprime o total de copos quebrados
print(total_copos_quebrados)
