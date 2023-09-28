def count_swaps(train):
    swaps = 0
    n = len(train)

    for i in range(n):
        for j in range(0, n - i - 1):
            if train[j] > train[j + 1]:
                train[j], train[j + 1] = train[j + 1], train[j]
                swaps += 1

    return swaps


def main():
    # Número de casos de teste
    num_cases = int(input("Número de casos de teste: "))

    for _ in range(num_cases):
        # Tamanho do trem
        l = int(input())

        # Permutação dos vagões
        train_order = list(map(int, input().split()))

        # Conta o número de swaps necessários
        swaps = count_swaps(train_order)

        # Imprime o resultado para o caso de teste atual
        print(f'Optimal train swapping takes {swaps} swaps.')


if __name__ == "__main__":
    main()
