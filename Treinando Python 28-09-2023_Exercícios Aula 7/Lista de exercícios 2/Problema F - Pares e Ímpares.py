# Função para ordenar os números conforme o critério
def ordenar_pares_impares(lista):
    # Separa os pares e ímpares
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]

    # Ordena os pares em ordem crescente
    pares.sort()

    # Ordena os ímpares em ordem decrescente
    impares.sort(reverse=True)

    # Retorna a lista final
    return pares + impares

# Número de casos de teste
n = int(input())

# Lista para armazenar os números de cada caso de teste
numeros = []

# Loop para ler os valores
for _ in range(n):
    valor = int(input())
    numeros.append(valor)

# Chamando a função e obtendo a lista ordenada
resultado = ordenar_pares_impares(numeros)

# Imprimindo o resultado
for num in resultado:
    print(num)
