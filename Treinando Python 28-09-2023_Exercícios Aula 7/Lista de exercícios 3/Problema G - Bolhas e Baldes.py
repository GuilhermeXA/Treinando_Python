def quem_ganha(N, sequencia):
    trocas = 0

    for i in range(N):
        if sequencia[i] != i + 1:
            j = sequencia.index(i + 1)
            sequencia[i], sequencia[j] = sequencia[j], sequencia[i]
            trocas += 1

    return "Carlos" if trocas % 2 == 0 else "Marcelo"


def main():
    while True:
        entrada = input().split()
        N = int(entrada[0])

        if N == 0:
            break

        sequencia = list(map(int, entrada[1:]))
        resultado = quem_ganha(N, sequencia)
        print(resultado)


if __name__ == "__main__":
    main()
