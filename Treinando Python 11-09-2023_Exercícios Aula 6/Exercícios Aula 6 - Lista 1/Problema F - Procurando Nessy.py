# Função para calcular o número mínimo de sonares
def calcular_minimo_sonares(n, m):
    # Calcula o número de janelas 5x5 em n e m
    janelas_n = (n - 4) // 5
    janelas_m = (m - 4) // 5

    # Calcula o número mínimo de sonares necessário
    minimo_sonares = janelas_n * janelas_m

    # Se houver colunas ou linhas extras, adiciona sonares adicionais
    if (n - 4) % 5 != 0:
        minimo_sonares += janelas_m
    if (m - 4) % 5 != 0:
        minimo_sonares += janelas_n

    return minimo_sonares

# Lê o número de casos de teste
t = int(input())

# Processa cada caso de teste
for _ in range(t):
    n, m = map(int, input().split())
    resultado = calcular_minimo_sonares(n, m)
    print(resultado)
