# Ler três valores inteiros
valores = list(map(int, input().split()))

# Ordenar os valores em ordem crescente
valores_ordenados = sorted(valores)

# Imprimir os valores em ordem crescente
for valor in valores_ordenados:
    print(valor)

# Imprimir uma linha em branco
print()

# Imprimir os valores na sequência como foram lidos
for valor in valores:
    print(valor)
