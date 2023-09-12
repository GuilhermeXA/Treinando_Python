def contar_picos(amostras):
    picos = 0

    for i in range(1, len(amostras) - 1):
        if amostras[i] > amostras[i - 1] and amostras[i] > amostras[i + 1]:
            picos += 1
        elif amostras[i] < amostras[i - 1] and amostras[i] < amostras[i + 1]:
            picos += 1

    return picos


while True:
    N = int(input())
    if N == 0:
        break

    amostras = list(map(int, input().split()))
    picos = contar_picos(amostras)

    print(picos)
