# Inicializar uma lista para armazenar os 100 valores
valores = []

# Ler 100 valores inteiros
for _ in range(100):
    valor = int(input())
    valores.append(valor)

# Encontrar o maior valor e sua posição
maior_valor = max(valores)
posicao_maior_valor = valores.index(maior_valor)

# Imprimir o maior valor e a posição
print(f"{maior_valor}\n{posicao_maior_valor + 1}")
