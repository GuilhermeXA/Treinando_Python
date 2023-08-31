def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])  # A soma de referência para verificar todas as linhas, colunas e diagonais

    # Verificar soma das linhas
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Verificar soma das colunas
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False

    # Verificar soma das diagonais
    diagonal_sum1 = sum(matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(matrix[i][n - 1 - i] for i in range(n))
    if diagonal_sum1 != target_sum or diagonal_sum2 != target_sum:
        return False

    return True


def main():
    n = int(input())  # Tamanho do quadrado
    matrix = [list(map(int, input().split())) for _ in range(n)]

    if is_magic_square(matrix):
        print(sum(matrix[0]))
    else:
        print("-1")


if __name__ == "__main__":
    main()
