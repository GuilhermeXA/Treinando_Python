def min_moves(s, t):
    moves = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            moves += 1
    return moves

def main():
    while True:
        s, t = input().split()
        if s == '*' and t == '*':
            break
        moves = min_moves(s, t)
        print(moves)

if __name__ == "__main__":
    main()
