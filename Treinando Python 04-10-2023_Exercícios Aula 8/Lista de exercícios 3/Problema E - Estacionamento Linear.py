def estacionamento_possivel(N, K, horarios):
    estacionamento = []

    for chegada, saida in horarios:
        while estacionamento and estacionamento[0] <= chegada:
            estacionamento.pop(0)

        if len(estacionamento) < K:
            estacionamento.append(saida)
        else:
            return "Nao"

    return "Sim"

def main():
    while True:
        N, K = map(int, input().split())
        if N == 0 and K == 0:
            break

        horarios = [tuple(map(int, input().split())) for _ in range(N)]

        resultado = estacionamento_possivel(N, K, horarios)
        print(resultado)

if __name__ == "__main__":
    main()
