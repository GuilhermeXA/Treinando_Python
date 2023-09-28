# Função para ordenar os números conforme o critério especificado
def ordenar_pares_impares(lista):
    # Separa pares e ímpares
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]

    # Ordena pares em ordem crescente
    pares.sort()

    # Ordena ímpares em ordem decrescente
    impares.sort(reverse=True)

    # Combina as duas listas ordenadas
    resultado = pares + impares

    return resultado

# Leitura do número de casos de teste
n = int(input("Digite o número de casos de teste: "))

# Lista para armazenar os resultados
resultados = []

# Loop para ler os valores de cada caso de teste
for _ in range(n):
    valores = list(map(int, input().split()))
    resultados.append(ordenar_pares_impares(valores))

# Imprime os resultados
for resultado in resultados:
    for valor in resultado:
        print(valor)
