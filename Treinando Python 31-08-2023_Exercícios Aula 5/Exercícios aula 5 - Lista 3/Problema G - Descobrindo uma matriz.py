def is_power_matrix(matrix):
    n = len(matrix)

    # Check the first column
    for i in range(n):
        if matrix[i][0] != 1:
            return False

    # Check the rest of the matrix
    for i in range(n):
        for j in range(1, n):
            if j != i + 1 and matrix[i][j] != matrix[i][1] ** (j - 1):
                return False

    return True


def swap_columns(matrix, x, y):
    for i in range(len(matrix)):
        matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def main():
    n = int(input())
    for _ in range(n):
        size = int(input())
        matrix = [list(map(int, input().split())) for _ in range(size)]

        if is_power_matrix(matrix):
            print("S")
        else:
            print("N")


if __name__ == "__main__":
    main()
