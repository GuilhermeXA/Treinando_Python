def insere_blocos(pilhas, fila):
    for bloco in fila:
        for i in range(len(pilhas)):
            if bloco == 1 and pilhas[i][-1] == 0:
                pilhas[i].pop()
                pilhas[i].append(1)
                break
    return pilhas

def imprime_pilhas(pilhas):
    for pilha in pilhas:
        print(" ".join(map(str, pilha)))

def main():
    while True:
        H, P, F = map(int, input().split())
        if H == 0 and P == 0 and F == 0:
            break

        pilhas = [list(map(int, input().split()))[::-1] for _ in range(H)]

        fila = list(map(int, input().split()))

        pilhas = insere_blocos(pilhas, fila)

        imprime_pilhas(pilhas)

if __name__ == "__main__":
    main()
