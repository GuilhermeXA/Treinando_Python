def tamanho_minimo_grupos(N, K, posicoes):
    posicoes.sort()

    tamanhos = [0] * (N - 1)

    for i in range(N - 1):
        tamanhos[i] = posicoes[i + 1] - posicoes[i]

    tamanhos.sort()

    soma_minima = sum(tamanhos[:-K + 1])

    return soma_minima

def main():
    while True:
        try:
            N, K = map(int, input().split())
            posicoes = list(map(int, input().split()))

            resultado = tamanho_minimo_grupos(N, K, posicoes)
            print(resultado)

        except EOFError:
            break

if __name__ == "__main__":
    main()
