def decode_matring(matring):
    F = int(matring[0])
    L = int(matring[1])
    N = len(matring) - 2
    decoded_string = ""

    for i in range(2, N + 2):
        Ci = (F * int(matring[i]) + L) % 257
        decoded_string += chr(Ci)

    return decoded_string

# Lê a entrada como uma lista de strings representando cada linha da matring
matring = [input() for _ in range(4)]

decoded_string = decode_matring(matring)
print(decoded_string)
