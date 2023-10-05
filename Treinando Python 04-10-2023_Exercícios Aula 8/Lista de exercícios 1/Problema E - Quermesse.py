def encontrar_ganhador(ingressos):
    for i, ingresso in enumerate(ingressos, start=1):
        if i == ingresso:
            return i


# Processamento dos conjuntos de teste
n_teste = 1
while True:
    # Leitura do número de participantes
    N = int(input())

    # Verificação de condição de parada
    if N == 0:
        break

    # Leitura dos ingressos dos participantes
    ingressos = list(map(int, input().split()))

    # Encontrar o ganhador
    ganhador = encontrar_ganhador(ingressos)

    # Saída formatada
    print(f'Teste {n_teste}')
    print(ganhador)
    print()

    # Atualização do número de teste
    n_teste += 1
