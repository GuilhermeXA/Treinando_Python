import re

def find_subsequence_positions(subsequence, sequence):
    positions = [m.start() for m in re.finditer(subsequence, sequence)]
    return positions

while True:
    try:
        n1 = input()
        n2 = input()

        positions = find_subsequence_positions(n1, n2)

        if positions:
            last_position = positions[-1]
            print(f"Qtd.Subsequencias: {len(positions)}")
            print(f"Pos: {last_position + 1}")
        else:
            print("Nao existe subsequencia")

    except EOFError:
        break
