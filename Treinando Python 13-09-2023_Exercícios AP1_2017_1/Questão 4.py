def lerVetor():
    n = int(input("Digite a quantidade de strings: "))
    lista = []
    for _ in range(n):
        string = input("Digite uma string: ")
        lista.append(string)
    return lista

def lerValor():
    valor = input("Digite a string a ser procurada: ")
    return valor

def buscaBinaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

# Programa principal
lista_ordenada = lerVetor()
valor_procurado = lerValor()
posicao = buscaBinaria(lista_ordenada, valor_procurado)

if posicao != -1:
    print(f"O valor foi encontrado na posição {posicao}")
else:
    print("Valor não encontrado")
