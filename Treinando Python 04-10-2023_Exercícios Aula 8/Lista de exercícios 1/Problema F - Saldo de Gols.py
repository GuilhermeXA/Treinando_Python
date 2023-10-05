def melhor_periodo(resultados):
    melhor_saldo = 0
    melhor_inicio = 0
    melhor_fim = 0

    saldo_atual = 0
    inicio_atual = 1

    for fim, (gols_a_favor, gols_contra) in enumerate(resultados, start=1):
        saldo_atual += gols_a_favor - gols_contra

        if saldo_atual > melhor_saldo or (
                saldo_atual == melhor_saldo and fim - inicio_atual > melhor_fim - melhor_inicio):
            melhor_saldo = saldo_atual
            melhor_inicio = inicio_atual
            melhor_fim = fim

        if saldo_atual <= 0:
            saldo_atual = 0
            inicio_atual = fim + 1

    return melhor_inicio, melhor_fim


# Processamento dos conjuntos de teste
n_teste = 1
while True:
    # Leitura do número de partidas
    N = int(input())

    # Verificação de condição de parada
    if N == 0:
        break

    # Leitura dos resultados das partidas
    resultados = [tuple(map(int, input().split())) for _ in range(N)]

    # Encontrar o melhor período
    inicio, fim = melhor_periodo(resultados)

    # Saída formatada
    print(f'Teste {n_teste}')
    if inicio == 0:
        print('nenhum')
    else:
        print(f'{inicio} {fim}')
    print()

    # Atualização do número de teste
    n_teste += 1
