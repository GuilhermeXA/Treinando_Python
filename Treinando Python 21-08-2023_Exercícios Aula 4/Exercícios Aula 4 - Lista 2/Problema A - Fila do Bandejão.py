while True:
    try:
        n, k = map(int, input().split())
        positions = list(map(int, input().split()))

        # Ordena as posições em ordem crescente
        positions.sort()

        # Calcula os tamanhos dos grupos e mantém os maiores K-1 tamanhos
        group_sizes = []
        for i in range(n - k):
            group_sizes.append(positions[i + 1] - positions[i])
        group_sizes.sort(reverse=True)

        # Soma os K-1 maiores tamanhos de grupo
        total_sum = sum(group_sizes[:k - 1])

        print(total_sum)

    except EOFError:
        break
