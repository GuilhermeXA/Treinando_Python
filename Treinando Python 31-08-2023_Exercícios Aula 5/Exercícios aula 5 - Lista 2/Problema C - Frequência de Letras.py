# Número de casos de teste
n = int(input())

# Processar cada caso de teste
for _ in range(n):
    texto = input().lower()  # Convertendo o texto para minúsculas
    frequencia = [0] * 26  # Lista para contar a frequência de cada letra

    for char in texto:
        if char.isalpha():  # Verificando se é uma letra
            index = ord(char) - ord('a')  # Calculando o índice da letra
            frequencia[index] += 1  # Incrementando a frequência da letra

    max_frequencia = max(frequencia)  # Encontrando a maior frequência
    letras_mais_frequentes = [chr(i + ord('a')) for i, freq in enumerate(frequencia) if freq == max_frequencia]

    print(''.join(letras_mais_frequentes))
