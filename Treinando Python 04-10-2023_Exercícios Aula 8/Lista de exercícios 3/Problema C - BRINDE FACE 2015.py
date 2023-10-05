def ganha_brinde(letras):
    painel = ['F', 'A', 'C', 'E']

    ganhadores = 0

    for letra in letras:
        painel.append(letra)
        if painel[-4:] == ['F', 'E', 'C', 'A']:
            ganhadores += 1

    return ganhadores

def main():
    casos_teste = int(input())

    for _ in range(casos_teste):
        num_participantes = int(input())
        letras_participantes = [input().split() for _ in range(num_participantes)]

        ganhadores = ganha_brinde([letra for sublist in letras_participantes for letra in sublist])

        print(ganhadores)

if __name__ == "__main__":
    main()
