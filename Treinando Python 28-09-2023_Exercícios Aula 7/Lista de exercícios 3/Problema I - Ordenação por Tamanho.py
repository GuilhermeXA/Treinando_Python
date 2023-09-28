def ordenar_strings_por_tamanho(strings):
    # Ordena a lista de strings por tamanho, e em caso de empate, mantém a ordem original
    strings.sort(key=lambda x: (len(x), strings.index(x)))

def main():
    try:
        n = int(input("Digite o número de casos de teste: "))
        conjunto_strings = []

        for _ in range(n):
            strings = input("Digite as strings separadas por espaços: ").split()
            conjunto_strings.extend(strings)

        ordenar_strings_por_tamanho(conjunto_strings)

        print("Conjunto ordenado:")
        for palavra in conjunto_strings:
            print(palavra, end=" ")
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer um número inteiro.")

if __name__ == "__main__":
    main()
