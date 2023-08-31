QT = int(input())  # Número de casos de teste

for _ in range(QT):
    jogador1, escolha1, jogador2, escolha2 = input().split()
    N, M = map(int, input().split())

    total = N + M

    if total % 2 == 0:
        vencedor = jogador1 if escolha1 == "PAR" else jogador2
    else:
        vencedor = jogador2 if escolha2 == "IMPAR" else jogador1

    print(vencedor)
