while True:
    n = int(input())

    if n == 0:
        break

    total_rectangles = 0

    for _ in range(n):
        c, v = map(int, input().split())
        total_rectangles += v // 2  # Cada par de varetas forma um retângulo

    total_rectangles //= 2  # Cada retângulo é formado por dois pares de varetas

    print(total_rectangles)
