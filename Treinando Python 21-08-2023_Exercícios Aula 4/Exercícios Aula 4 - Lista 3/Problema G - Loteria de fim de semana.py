while True:
    N, C, K = map(int, input().split())
    if N == 0 and C == 0 and K == 0:
        break

    # Inicializar um dicionário para contar a frequência dos números sorteados
    freq = {i: 0 for i in range(1, K + 1)}

    # Contar a frequência dos números sorteados em cada concurso prévio
    for _ in range(N):
        numbers = list(map(int, input().split()))
        for num in numbers:
            freq[num] += 1

    # Encontrar o menor número de vezes que um número foi sorteado
    min_freq = min(freq.values())

    # Encontrar os números que foram sorteados o menor número de vezes
    least_frequent_numbers = [num for num, f in freq.items() if f == min_freq]

    # Ordenar a lista em ordem crescente e imprimir
    least_frequent_numbers.sort()
    print(*least_frequent_numbers)
