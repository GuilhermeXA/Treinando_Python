def is_fibonacci(n):
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return b == n

def has_digit_3(n):
    return '3' in str(n)

def is_multiple_of_3(n):
    return n % 3 == 0

def threebonacci_sequence(n):
    sequence = []
    num = 1
    while len(sequence) < n:
        if is_fibonacci(num) and (has_digit_3(num) or is_multiple_of_3(num)):
            sequence.append(num)
        num += 1
    return sequence

def main():
    while True:
        try:
            n = int(input())
            sequence = threebonacci_sequence(n)
            for num in sequence:
                print(num)
        except EOFError:
            break

if __name__ == "__main__":
    main()
