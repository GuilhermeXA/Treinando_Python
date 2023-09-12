import re

while True:
    try:
        N1 = input()
        N2 = input()

        if re.search(f".*{''.join(N1)}.*", N2):
            start = N2.index(N1[0]) + 1
            positions = [i for i, c in enumerate(N2) if c == N1[0]]

            for pos in positions:
                if N2[pos:pos + len(N1)] == N1:
                    start = pos + 1

            print(f"Numero {N1} esta na posicao {start}")
        else:
            print("Nao existe subsequencia")

    except EOFError:
        break
