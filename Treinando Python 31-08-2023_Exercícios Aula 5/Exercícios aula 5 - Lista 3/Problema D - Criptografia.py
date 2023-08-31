def criptografar(texto):
    cripto_texto = ""

    for char in texto:
        if char.isalpha():
            cripto_texto += chr(ord(char) + 3) if char.islower() else chr(ord(char) + 3).lower()
        else:
            cripto_texto += char

    cripto_texto = cripto_texto[::-1]

    meio = len(cripto_texto) // 2
    for i in range(meio, len(cripto_texto)):
        cripto_texto = cripto_texto[:i] + chr(ord(cripto_texto[i]) - 1) + cripto_texto[i + 1:]

    return cripto_texto


def main():
    n = int(input())
    for _ in range(n):
        linha = input()
        cripto = criptografar(linha)
        print(cripto)


if __name__ == "__main__":
    main()
