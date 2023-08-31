def main():
    while True:
        n = int(input())  # Número de palavras no caso de teste
        if n == 0:
            break

        words = []
        max_length = 0

        for _ in range(n):
            word = input()
            words.append(word)
            max_length = max(max_length, len(word))

        for word in words:
            spaces = max_length - len(word)
            print(" " * spaces + word)

        print()  # Linha em branco entre os casos de teste


if __name__ == "__main__":
    main()
