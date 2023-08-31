def main():
    n = int(input())
    x = 4
    for _ in range(n):
        m = int(input())
        matrix = []
        for _ in range(m):
            row = list(map(int, input().split()))
            matrix.append(row)

        print(f"Quadrado da matriz #{x}:")
        for i in range(m):
            for j in range(m):
                squared_value = matrix[i][j] * matrix[i][j]
                if j == m - 1:
                    print(f"{squared_value}")
                else:
                    print(f"{squared_value:>10}", end=" ")

        print()
        x += 1


if __name__ == "__main__":
    main()
