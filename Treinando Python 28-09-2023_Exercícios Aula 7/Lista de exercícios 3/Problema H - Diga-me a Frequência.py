from collections import Counter


def contar_caracteres(texto):
    contador = Counter(texto)
    caracteres_ordenados = sorted(contador.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)

    for caractere, frequencia in caracteres_ordenados:
        print(f"{ord(caractere)} {frequencia}")


def main():
    while True:
        try:
            linha = input()
            contar_caracteres(linha)
            print()  # Linha em branco entre os conjuntos de saída
        except EOFError:
            break


if __name__ == "__main__":
    main()
