def check_row(matrix, row):
    return set(matrix[row]) == set(range(1, 10))


def check_column(matrix, col):
    column = [matrix[row][col] for row in range(9)]
    return set(column) == set(range(1, 10))


def check_subgrid(matrix, start_row, start_col):
    subgrid = [matrix[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
    return set(subgrid) == set(range(1, 10))


def is_sudoku_solution(matrix):
    for i in range(9):
        if not (check_row(matrix, i) and check_column(matrix, i)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_subgrid(matrix, i, j):
                return False

    return True


def main():
    n = int(input())  # Número de instâncias
    for instance in range(1, n + 1):
        matrix = [list(map(int, input().split())) for _ in range(9)]

        print(f"Instancia {instance}")
        if is_sudoku_solution(matrix):
            print("SIM")
        else:
            print("NAO")

        print()  # Linha em branco após cada instância


if __name__ == "__main__":
    main()
