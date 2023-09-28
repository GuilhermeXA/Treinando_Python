# Inicializar um contador para armazenar a quantidade de valores positivos
quantidade_positivos = 0

# Ler seis valores
for _ in range(6):
    valor = float(input())

    # Verificar se o valor é positivo
    if valor > 0:
        quantidade_positivos += 1

# Imprimir a quantidade de valores positivos
print(f"{quantidade_positivos} valores positivos foram digitados.")
