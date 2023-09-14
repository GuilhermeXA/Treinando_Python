'''
Exercício 5: Escreva uma função que receba uma
lista de palavras como argumento e retorne uma
lista contendo o número de letras de cada palavra.
'''

'''
listaPalavras = []
while True:
    palavra = str(input('Digite uma palavra: '))
    if palavra == '':
        break
    listaPalavras.append(palavra)


numLetras = 0
listaNumLetras = []
for i in listaPalavras:
    listaNumLetras.append(len(i))

print(f'As palavras digitadas são {listaPalavras}')

for j in listaPalavras:
    for k in listaNumLetras:
        print(f'A palavra {j} tem {k} letras')
'''


def contar_letras(lista_palavras):
    # Cria uma lista vazia para armazenar o número de letras de cada palavra
    num_letras = []

    # Itera sobre cada palavra na lista de palavras
    for palavra in lista_palavras:
        # Adiciona o número de letras da palavra à lista num_letras
        num_letras.append(len(palavra))

    return num_letras


# Exemplo de uso da função:
lista_de_palavras = ["python", "programacao", "exercicio", "lista"]
resultado = contar_letras(lista_de_palavras)
print(resultado)  # Isso irá imprimir [6, 11, 8, 5]
