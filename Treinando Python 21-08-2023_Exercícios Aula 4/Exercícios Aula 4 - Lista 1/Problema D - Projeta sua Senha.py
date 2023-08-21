def decode_password(associations, encoded_password):
    mapping = {}  # Dicionário para mapear dígitos para letras

    for i in range(len(associations)):
        digits = associations[i][:2]  # Os dois primeiros dígitos são para a letra atual
        letter = chr(ord('A') + i)  # Determina a letra correspondente

        for digit in digits:
            mapping[digit] = letter

    decoded_password = [mapping[digit] for digit in encoded_password]
    return ''.join(decoded_password)

test_number = 1
while True:
    n = int(input())
    if n == 0:
        break

    associations = []
    for _ in range(n):
        digits = input()  # Dígitos associados a cada letra
        associations.append(digits)

    encoded_password = input()  # Senha codificada

    decoded_password = decode_password(associations, encoded_password)

    print(f"Teste {test_number}")
    print(decoded_password)
    print()  # Linha em branco após cada conjunto de testes
    test_number += 1
