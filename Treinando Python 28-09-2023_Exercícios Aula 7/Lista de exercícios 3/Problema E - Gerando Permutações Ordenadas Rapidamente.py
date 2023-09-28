def gerar_permutacoes(prefixo, sufixo):
    if len(sufixo) == 0:
        print(prefixo)
    else:
        for i in range(len(sufixo)):
            nova_prefixo = prefixo + sufixo[i]
            novo_sufixo = sufixo[:i] + sufixo[i + 1:]
            gerar_permutacoes(nova_prefixo, novo_sufixo)

# Função principal para gerar permutações para cada string
def main():
    # Número de strings
    n = int(input())

    for _ in range(n):
        # String de entrada
        string_entrada = input()

        # Ordena a string para garantir a ordem lexicográfica crescente
        string_ordenada = ''.join(sorted(string_entrada))

        # Chama a função de geração de permutações
        gerar_permutacoes('', string_ordenada)

        # Imprime uma linha em branco após cada lista de permutações
        print()

if __name__ == "__main__":
    main()
