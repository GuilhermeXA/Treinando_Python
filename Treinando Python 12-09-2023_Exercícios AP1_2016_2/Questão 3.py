# Subprograma para criar e preencher a matriz 5x5 com palavras
def criar_matriz():
    matriz = []
    for _ in range(5):
        linha = input("Digite uma linha de 5 palavras separadas por espaço: ").split()
        matriz.append(linha)
    return matriz


# Subprograma para exibir a matriz de forma amigável
def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))


# Subprograma para procurar uma palavra na matriz
def procurar_palavra(matriz, palavra):
    for i, linha in enumerate(matriz):
        for j, palavra_na_matriz in enumerate(linha):
            if palavra_na_matriz == palavra:
                return i, j
    return None


# Programa principal
matriz = criar_matriz()
mostrar_matriz(matriz)

while True:
    palavra_consulta = input("Digite uma palavra para consultar na matriz (ou 'Fim' para encerrar): ")

    if palavra_consulta.lower() == 'fim':
        break

    resultado = procurar_palavra(matriz, palavra_consulta)

    if resultado:
        print(f"A palavra '{palavra_consulta}' foi encontrada na linha {resultado[0] + 1} e coluna {resultado[1] + 1}.")
    else:
        print("Palavra não encontrada.")
