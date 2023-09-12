# Lê a letra de interesse
letra = input()

# Lê o texto
texto = input().split()

# Inicializa a contagem de palavras com a letra
palavras_com_letra = 0

# Percorre as palavras no texto
for palavra in texto:
    if letra in palavra:
        palavras_com_letra += 1

# Calcula a porcentagem
porcentagem = (palavras_com_letra / len(texto)) * 100

# Imprime a porcentagem com uma casa decimal
print(f'{porcentagem:.1f}')
