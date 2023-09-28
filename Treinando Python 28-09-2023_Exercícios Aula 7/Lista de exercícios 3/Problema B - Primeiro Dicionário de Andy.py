def extract_words(text):
    # Converte o texto para minúsculas e separa as palavras
    words = text.lower().split()
    # Remove caracteres especiais ao redor das palavras
    words = [word.strip('.,?!()[]{}"\'') for word in words]
    return words

def main():
    # Lista para armazenar palavras distintas
    unique_words = set()

    # Loop para ler as linhas de entrada
    while True:
        try:
            line = input()
            words = extract_words(line)
            unique_words.update(words)
        except EOFError:
            break

    # Ordena e imprime as palavras distintas
    sorted_words = sorted(unique_words)
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
