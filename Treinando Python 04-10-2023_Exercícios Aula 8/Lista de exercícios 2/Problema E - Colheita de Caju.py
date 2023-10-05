def max_produtividade(L, C, M, N, fazenda):
    max_prod = 0

    for i in range(L - M + 1):
        for j in range(C - N + 1):
            area = [linha[j:j + N] for linha in fazenda[i:i + M]]
            prod = sum(sum(linha) for linha in area)
            max_prod = max(max_prod, prod)

    return max_prod

def main():
    L, C, M, N = map(int, input().split())
    fazenda = [list(map(int, input().split())) for _ in range(L)]

    resultado = max_produtividade(L, C, M, N, fazenda)
    print(resultado)

if __name__ == "__main__":
    main()
