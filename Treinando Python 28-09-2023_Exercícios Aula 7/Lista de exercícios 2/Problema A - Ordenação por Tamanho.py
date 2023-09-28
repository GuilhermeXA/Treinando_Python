# Função para ordenar o conjunto de strings pelo tamanho
def ordenar_por_tamanho(conjunto):
    # Usando a função sorted com uma chave personalizada para ordenar pelo tamanho
    resultado = sorted(conjunto, key=lambda x: (len(x), conjunto.index(x)))
    return resultado

# Lendo o número de casos de teste
num_casos = int(input())

# Loop pelos casos de teste
for _ in range(num_casos):
    # Lendo o conjunto de strings
    conjunto_strings = input().split()

    # Chamando a função para ordenar o conjunto pelo tamanho
    resultado = ordenar_por_tamanho(conjunto_strings)

    # Imprimindo o resultado
    print(" ".join(resultado))
