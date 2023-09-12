def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return j == len(t)


# Lê o número de casos de teste
N = int(input())

for _ in range(N):
    # Lê a sequência principal S
    S = input().strip()

    # Lê o número de queries
    Q = int(input())

    for _ in range(Q):
        # Lê a sequência R
        R = input().strip()

        # Verifica se R é uma subsequência de S
        if is_subsequence(S, R):
            print("Yes")
        else:
            print("No")
