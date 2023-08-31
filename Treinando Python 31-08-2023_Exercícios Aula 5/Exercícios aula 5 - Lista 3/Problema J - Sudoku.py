def is_valid_sudoku(matrix):
    # Verificar as linhas
    for row in matrix:
        if len(set(row)) != 9:
            return False

    # Verificar as colunas
    for col in range(9):
        if len(set(matrix[row][col] for row in range(9))) != 9:
            return False

    # Verificar as regiões 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            region = [matrix[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(region)) != 9:
                return False

    return True


def main():
    N = int(input())
    for instance in range(1, N + 1):
        matrix = [list(map(int, input().split())) for _ in range(9)]
        print(f"Instancia {instance}")
        if is_valid_sudoku(matrix):
            print("SIM")
        else:
            print("NAO")
        print()


if __name__ == "__main__":
    main()
