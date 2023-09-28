def decifra_cesar(sentenca, deslocamento):
    decifrado = ''
    for letra in sentenca:
        if letra.isalpha():
            # Calculando o deslocamento considerando a base ASCII
            nova_letra = chr((ord(letra) - deslocamento - ord('A')) % 26 + ord('A'))
            decifrado += nova_letra
        else:
            # Se não for uma letra, adiciona o caractere original
            decifrado += letra
    return decifrado

# Lendo o número de casos de teste
num_casos = int(input())

# Loop pelos casos de teste
for _ in range(num_casos):
    # Lendo a sentença cifrada e o deslocamento
    sentenca_cifrada = input().strip()
    deslocamento = int(input())

    # Chamando a função de decifração e imprimindo o resultado
    resultado = decifra_cesar(sentenca_cifrada, deslocamento)
    print(resultado)
