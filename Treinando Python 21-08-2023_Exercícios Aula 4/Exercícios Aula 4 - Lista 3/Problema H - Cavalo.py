def is_valid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


def bfs(start_x, start_y, peons, N, M):
    visited = [[False] * M for _ in range(N)]
    queue = [(start_x, start_y, 0)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.pop(0)

        if (x, y) in peons:
            peons.remove((x, y))
            if not peons:
                return moves

        for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, N, M) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1))


while True:
    N, M, K = map(int, input().split())
    if N == 0 and M == 0 and K == 0:
        break

    board = [input() for _ in range(N)]
    peons = []
    start_x, start_y = 0, 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'C':
                start_x, start_y = i, j
            elif board[i][j] == 'P':
                peons.append((i, j))

    moves = bfs(start_x, start_y, peons, N, M)
    print(moves)

