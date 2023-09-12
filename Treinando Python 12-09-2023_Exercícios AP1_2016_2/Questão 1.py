import random

# Função para gerar um vetor de números de ponto flutuante aleatórios
def gerar_vetor(tamanho):
    return [random.random() for _ in range(tamanho)]

# Função para ordenar um vetor usando o algoritmo Selection Sort
def selection_sort(vetor):
    tamanho = len(vetor)
    for i in range(tamanho - 1):
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

# Função para imprimir um vetor
def imprimir_vetor(vetor):
    for elemento in vetor:
        print(elemento, end=" ")
    print()

# Programa principal
if __name__ == "__main__":
    tamanho_vetor = int(input("Digite o tamanho do vetor: "))
    vetor_desordenado = gerar_vetor(tamanho_vetor)

    print("Vetor gerado:")
    imprimir_vetor(vetor_desordenado)

    selection_sort(vetor_desordenado)

    print("\nVetor ordenado:")
    imprimir_vetor(vetor_desordenado)
