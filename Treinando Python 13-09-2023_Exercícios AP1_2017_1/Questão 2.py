import random

# Função para criar uma matriz com números aleatórios no intervalo [10, 99]
def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = [random.randint(10, 99) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

# Função para calcular a soma de uma linha da matriz
def soma_linha(matriz, linha):
    return sum(matriz[linha])

# Função para calcular a soma de uma coluna da matriz
def soma_coluna(matriz, coluna):
    return sum(matriz[i][coluna] for i in range(len(matriz)))

# Função para encontrar a linha de maior soma
def linha_maior_soma(matriz):
    maior_soma = -1
    linha_maior = None
    for i in range(len(matriz)):
        soma = soma_linha(matriz, i)
        if soma > maior_soma:
            maior_soma = soma
            linha_maior = matriz[i]
    return linha_maior

# Função para encontrar a coluna de maior soma
def coluna_maior_soma(matriz):
    maior_soma = -1
    coluna_maior = None
    for j in range(len(matriz[0])):
        soma = soma_coluna(matriz, j)
        if soma > maior_soma:
            maior_soma = soma
            coluna_maior = [matriz[i][j] for i in range(len(matriz))]
    return coluna_maior

# Entrada de dados
L, C = map(int, input("Digite a quantidade de linhas e colunas (L C): ").split())

# Cria a matriz
matriz = criar_matriz(L, C)

# Mostra o conteúdo da matriz
for linha in matriz:
    print(*linha)

print()  # Linha em branco

# Encontra a linha de maior soma
linha_maior = linha_maior_soma(matriz)

# Mostra o conteúdo da linha de maior soma
print(*linha_maior)

print()  # Linha em branco

# Encontra a coluna de maior soma
coluna_maior = coluna_maior_soma(matriz)

# Mostra o conteúdo da coluna de maior soma
for valor in coluna_maior:
    print(valor)
