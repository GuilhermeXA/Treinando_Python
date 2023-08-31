def is_valid(rival_list, rival):
    for i, rival_idx in enumerate(rival_list):
        if rival_idx == rival:
            return False
        if len(rival_list[i:]) >= rival:
            if rival_list[i:i+rival].count(rival) != rival - 1:
                return False
    return True

def solve(rival_lists, current_list, idx, N):
    if idx == N:
        return current_list
    for rival in range(2, N + 1):
        if is_valid(current_list, rival):
            updated_list = current_list + [rival]
            result = solve(rival_lists, updated_list, idx + 1, N)
            if result is not None:
                return result
    return None

def main():
    while True:
        N = int(input())
        if N == -1:
            break
        rival_lists = [list(map(int, input().split())) for _ in range(N - 1)]
        result = solve(rival_lists, [1], 1, N)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
