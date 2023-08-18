# Leitura dos valores
valores = list(map(int, input().split()))

# Ordena os valores em ordem crescente
valores_ordenados = sorted(valores)

# Imprime os valores ordenados
for valor in valores_ordenados:
    print(valor)

# Imprime uma linha em branco
print()

# Imprime os valores na sequência original
for valor in valores:
    print(valor)
