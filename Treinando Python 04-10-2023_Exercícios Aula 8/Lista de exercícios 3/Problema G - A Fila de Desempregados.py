def choose_candidates(N, k, m):
    candidates = list(range(1, N + 1))
    result = []

    i, j = 0, N - 1

    while candidates:
        i = (i + k - 1) % len(candidates)
        j = (j - m + 1) % len(candidates)

        if i == j:
            result.append(candidates.pop(i))
        else:
            result.append(candidates.pop(i))
            result.append(candidates.pop(j))

    return result

def main():
    while True:
        N, k, m = map(int, input().split())

        if N == 0 and k == 0 and m == 0:
            break

        result = choose_candidates(N, k, m)
        result = map(str, result)
        print(', '.join(result))

if __name__ == "__main__":
    main()
