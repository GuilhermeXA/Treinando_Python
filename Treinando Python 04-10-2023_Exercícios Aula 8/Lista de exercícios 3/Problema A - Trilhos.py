def pode_reorganizar(vagoes, ordem_desejada):
    estacao = []
    i = 1

    for vagao_desejado in ordem_desejada:
        while i <= len(vagoes) or (len(estacao) > 0 and estacao[-1] == vagao_desejado):
            if len(estacao) > 0 and estacao[-1] == vagao_desejado:
                estacao.pop()
                break
            else:
                estacao.append(vagoes[i - 1])
                i += 1

    return len(estacao) == 0

def main():
    while True:
        N = int(input())
        if N == 0:
            break

        vagoes = list(map(int, input().split()))
        while True:
            ordem_desejada = list(map(int, input().split()))
            if ordem_desejada[0] == 0:
                break

            resultado = "Yes" if pode_reorganizar(vagoes, ordem_desejada) else "No"
            print(resultado)

        print()

if __name__ == "__main__":
    main()
