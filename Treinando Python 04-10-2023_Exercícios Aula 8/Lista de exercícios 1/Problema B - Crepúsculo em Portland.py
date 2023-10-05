def verifica_quadras(mapa):
    n = len(mapa) - 1
    resultado = []

    for i in range(n):
        linha_resultado = ""
        for j in range(n):
            # Verifica se existem câmeras em pelo menos duas esquinas da quadra
            cameras = (
                mapa[i][j] + mapa[i + 1][j] + mapa[i][j + 1] + mapa[i + 1][j + 1]
            )
            if cameras >= 2:
                linha_resultado += "S"
            else:
                linha_resultado += "U"

        resultado.append(linha_resultado)

    return resultado

# Leitura da entrada
N = int(input())
mapa = [list(map(int, input().split())) for _ in range(N + 1)]

# Verifica o status das quadras
status_quadras = verifica_quadras(mapa)

# Saída
for linha in status_quadras:
    print(linha)
