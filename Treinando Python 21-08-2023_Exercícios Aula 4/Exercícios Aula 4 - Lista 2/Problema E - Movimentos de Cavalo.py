# Movimentos possíveis do cavalo em forma de pares de deslocamento (linha, coluna)
moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]


def valid_position(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def bfs(start, end):
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = [(start, 0)]

    while queue:
        position, moves_count = queue.pop(0)

        if position == end:
            return moves_count

        row, col = position
        visited[row][col] = True

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if valid_position(new_row, new_col) and not visited[new_row][new_col]:
                queue.append(((new_row, new_col), moves_count + 1))
                visited[new_row][new_col] = True


while True:
    try:
        a, b = input().split()
        start = (int(a[1]) - 1, ord(a[0]) - ord('a'))
        end = (int(b[1]) - 1, ord(b[0]) - ord('a'))

        moves_count = bfs(start, end)

        print(f"To get from {a} to {b} takes {moves_count} knight moves.")

    except EOFError:
        break
