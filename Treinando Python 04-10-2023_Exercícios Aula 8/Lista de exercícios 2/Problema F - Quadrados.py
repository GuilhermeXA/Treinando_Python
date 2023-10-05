def eh_quadrado_magico(quadrado):
    N = len(quadrado)
    soma_referencia = sum(quadrado[0])

    # Verifica as somas das linhas
    for linha in quadrado:
        if sum(linha) != soma_referencia:
            return -1

    # Verifica as somas das colunas
    for coluna in range(N):
        soma_coluna = sum(linha[coluna] for linha in quadrado)
        if soma_coluna != soma_referencia:
            return -1

    # Verifica a soma da diagonal principal
    soma_diagonal_principal = sum(quadrado[i][i] for i in range(N))
    if soma_diagonal_principal != soma_referencia:
        return -1

    # Verifica a soma da diagonal secundária
    soma_diagonal_secundaria = sum(quadrado[i][N - i - 1] for i in range(N))
    if soma_diagonal_secundaria != soma_referencia:
        return -1

    return soma_referencia

def main():
    N = int(input())
    quadrado = [list(map(int, input().split())) for _ in range(N)]

    resultado = eh_quadrado_magico(quadrado)
    print(resultado)

if __name__ == "__main__":
    main()
