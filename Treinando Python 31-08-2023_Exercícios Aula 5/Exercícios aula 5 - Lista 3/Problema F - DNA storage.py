def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def min_transformations(chains):
    n = len(chains)
    min_transforms = float('inf')

    for i in range(n):
        total_transforms = 0
        for j in range(n):
            total_transforms += hamming_distance(chains[i], chains[j])
        min_transforms = min(min_transforms, total_transforms)

    return min_transforms


def main():
    instance = 1

    while True:
        n, m = map(int, input().split())
        if n == 0:
            break

        chains = [input() for _ in range(n)]
        min_transforms = min_transformations(chains)

        print(f"Instancia {instance}")
        print(min_transforms)
        print()

        instance += 1


if __name__ == "__main__":
    main()
