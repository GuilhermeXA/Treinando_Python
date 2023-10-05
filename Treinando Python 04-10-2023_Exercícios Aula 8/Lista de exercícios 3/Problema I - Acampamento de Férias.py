def brincadeira_gincana(N, criancas):
    sentido_horario = True
    indice = 0

    while len(criancas) > 1:
        valor = criancas[indice][1]

        if valor % 2 == 0:
            sentido_horario = not sentido_horario
        else:
            sentido_horario = sentido_horario

        if sentido_horario:
            indice = (indice + valor - 1) % len(criancas)
        else:
            indice = (indice - valor + 1) % len(criancas)

        criancas.pop(indice)

        if sentido_horario:
            if indice == len(criancas):
                indice = 0

    return criancas[0][0]

def main():
    while True:
        N = int(input())
        if N == 0:
            break

        criancas = [input().split() for _ in range(N)]

        vencedor = brincadeira_gincana(N, criancas)

        print(f"Vencedor(a): {vencedor}")

if __name__ == "__main__":
    main()
