def solve_sequence(digit1, letter, digit2):
    if letter.isupper():
        return int(digit2) - int(digit1)
    elif letter.islower():
        return int(digit1) + int(digit2)
    elif digit1 == digit2:
        return int(digit1) * int(digit2)


def main():
    n = int(input())

    for _ in range(n):
        sequence = input().strip()
        digit1, letter, digit2 = sequence[0], sequence[1], sequence[2]

        result = solve_sequence(digit1, letter, digit2)
        print(result)


if __name__ == "__main__":
    main()
