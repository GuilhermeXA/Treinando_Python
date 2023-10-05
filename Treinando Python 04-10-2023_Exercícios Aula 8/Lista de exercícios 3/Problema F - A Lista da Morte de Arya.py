class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result


def main():
    n = int(input())
    enemies = list(map(int, input().split()))

    fenwick_tree = FenwickTree(n)
    idx_map = {}

    for idx, enemy in enumerate(enemies, start=1):
        fenwick_tree.update(idx, 1)
        idx_map[enemy] = idx

    q = int(input())

    for _ in range(q):
        operation = input().split()
        if operation[0] == 'I':
            p, e = map(int, operation[1:])
            idx = idx_map[e]
            fenwick_tree.update(idx, -1)
            fenwick_tree.update(idx + 1, 1)
            idx_map[p] = idx + 1
        elif operation[0] == 'R':
            e = int(operation[1])
            idx = idx_map[e]
            fenwick_tree.update(idx, -1)
        elif operation[0] == 'Q':
            a, b = map(int, operation[1:])
            result = fenwick_tree.query(b) - fenwick_tree.query(a - 1)
            print(result)

if __name__ == "__main__":
    main()
