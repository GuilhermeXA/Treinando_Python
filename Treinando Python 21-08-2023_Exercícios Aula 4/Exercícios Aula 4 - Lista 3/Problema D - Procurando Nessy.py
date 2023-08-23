# Função para calcular o menor número de sonares
def calcular_sonares(n, m):
    # Se a grade for 6x6 ou menor, 1 sonar é suficiente para cobrir tudo
    if n <= 6 or m <= 6:
        return 1

    # Se a grade for maior do que 6x6, calcula o número mínimo de sonares
    # necessário para cobrir todas as posições
    return (n + 6 - 1) // 6 * ((m + 6 - 1) // 6)


# Lê o número de casos de teste
t = int(input())

# Processa cada caso de teste
for _ in range(t):
    n, m = map(int, input().split())
    sonares = calcular_sonares(n, m)
    print(sonares)
