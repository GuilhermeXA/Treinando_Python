# Função para gerar a sequência de granizo
def granizo_sequence(h):
    sequence = [h]

    while h != 1:
        if h % 2 == 0:
            h //= 2
        else:
            h = 3 * h + 1
        sequence.append(h)

    return sequence


# Lê os valores de entrada até encontrar um 0
while True:
    H = int(input())
    if H == 0:
        break

    sequence = granizo_sequence(H)
    max_number = max(sequence)
    print(max_number)
