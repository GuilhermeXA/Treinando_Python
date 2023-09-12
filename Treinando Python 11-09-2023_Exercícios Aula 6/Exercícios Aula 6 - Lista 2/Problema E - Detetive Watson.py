while True:
    N = int(input())
    if N == 0:
        break

    suspeitos = list(map(int, input().split()))

    segundo_mais_suspeito = sorted(range(N), key=lambda i: suspeitos[i])[1]

    print(segundo_mais_suspeito + 1)
