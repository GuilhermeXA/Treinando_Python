while True:
    n = int(input())

    if n == 0:
        break

    suspeitos = list(map(int, input().split()))

    segundo_mais_suspeito = sorted(suspeitos)[-2]  # Encontra o segundo mais suspeito
    indice_assassino = suspeitos.index(segundo_mais_suspeito) + 1

    print(indice_assassino)
