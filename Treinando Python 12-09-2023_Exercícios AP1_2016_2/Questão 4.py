import random


# Subprograma para solicitar as dimensões da matriz
def solicitar_dimensoes():
    linhas = int(input("Digite a quantidade de linhas da matriz: "))
    colunas = int(input("Digite a quantidade de colunas da matriz: "))
    return linhas, colunas


# Subprograma para criar e preencher a matriz aleatoriamente
def criar_e_preencher_matriz(linhas, colunas):
    matriz = [[random.randint(-10, 10) for _ in range(colunas)] for _ in range(linhas)]
    return matriz


# Subprograma para exibir uma matriz ou submatriz
def exibir_matriz(matriz, linha_inicial, linha_final, coluna_inicial, coluna_final):
    for i in range(linha_inicial, linha_final + 1):
        for j in range(coluna_inicial, coluna_final + 1):
            print(matriz[i][j], end=" ")
        print()


# Programa principal
linhas, colunas = solicitar_dimensoes()
matriz = criar_e_preencher_matriz(linhas, colunas)

if linhas < 3 or colunas < 3:
    print("A matriz é muito pequena.")
else:
    print("Matriz completa:")
    exibir_matriz(matriz, 0, linhas - 1, 0, colunas - 1)

    print("\nSubmatrizes 3x3:")
    for i in range(linhas - 2):
        for j in range(colunas - 2):
            exibir_matriz(matriz, i, i + 2, j, j + 2)
            print()

