def sequencia_movimentos(N, entrada, saida):
    estacao = []
    movimentos = []

    i = 0
    j = 0

    while j < N:
        if len(estacao) > 0 and estacao[-1] == saida[j]:
            estacao.pop()
            movimentos.append('R')
            j += 1
        elif i < N:
            estacao.append(entrada[i])
            movimentos.append('I')
            i += 1
        else:
            break

    if j == N:
        return movimentos
    else:
        return "Impossible"

def main():
    while True:
        N = int(input())
        if N == 0:
            break

        entrada = input().strip()
        saida_desejada = input().strip()

        movimentos = sequencia_movimentos(N, entrada, saida_desejada)

        if movimentos == "Impossible":
            print("Impossible")
        else:
            print(" ".join(movimentos))

        print()

if __name__ == "__main__":
    main()
