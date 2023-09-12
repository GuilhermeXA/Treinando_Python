def ganhar_o_jogo(N, P):
    dp = [False] * (N + 1)
    dp[0] = True

    for i in range(1, N + 1):
        if dp[i - 1] and P[i - 1] > 0:
            dp[i] = True
            for j in range(i + 1, min(N + 1, i + P[i - 1] + 1)):
                P[j - 1] -= 1

    return dp[N]

while True:
    N = int(input())
    if N == -1:
        break
    P = list(map(int, input().split()))
    result = ganhar_o_jogo(N, P)
    if result:
        print('S')
    else:
        print('N')
