def main():
    n = int(input())
    for _ in range(n):
        text = input().lower()  # Transforma o texto em minúsculas
        letter_count = [0] * 26  # Lista para contar a frequência de cada letra

        for char in text:
            if char.isalpha():
                letter_count[ord(char) - ord('a')] += 1

        max_frequency = max(letter_count)  # Maior frequência de letra(s)

        most_frequent_letters = []
        for i in range(26):
            if letter_count[i] == max_frequency:
                most_frequent_letters.append(chr(ord('a') + i))

        print(''.join(most_frequent_letters))


if __name__ == "__main__":
    main()
