import random

# Função para gerar uma matriz de dimensões (linhas x colunas) com valores aleatórios de 0 a 9
def gerar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(0, 9) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

# Função para calcular a média dos valores em uma matriz
def calcular_media(matriz):
    soma = 0
    total_elementos = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
            total_elementos += 1
    if total_elementos == 0:
        return 0
    return soma / total_elementos

# Função para verificar se uma linha possui todos os valores acima da média
def linha_acima_da_media(linha, media):
    return all(valor > media for valor in linha)

# Leitura das dimensões da matriz
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

# Geração da matriz aleatória
matriz = gerar_matriz(linhas, colunas)

# Exibição da matriz
for linha in matriz:
    print(" ".join(map(str, linha)))

print()

# Cálculo da média
media = calcular_media(matriz)
print(f"Média dos valores na matriz: {media:.2f}")

print()

# Linhas com todos os valores acima da média
for i, linha in enumerate(matriz):
    if linha_acima_da_media(linha, media):
        print(f"Linha {i + 1}: {' '.join(map(str, linha))}")
