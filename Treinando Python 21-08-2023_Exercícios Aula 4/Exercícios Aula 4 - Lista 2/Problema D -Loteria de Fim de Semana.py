while True:
    n, c, k = map(int, input().split())

    if n == 0 and c == 0 and k == 0:
        break

    number_counts = [0] * (k + 1)  # Inicializa a contagem de cada número

    for _ in range(n):
        drawn_numbers = list(map(int, input().split()))
        for num in drawn_numbers:
            number_counts[num] += 1

    min_count = min(number_counts)

    least_drawn_numbers = [str(num) for num, count in enumerate(number_counts) if count == min_count]

    print(" ".join(least_drawn_numbers))
