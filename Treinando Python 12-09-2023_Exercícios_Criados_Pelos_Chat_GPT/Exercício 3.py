'''
Exercício 3: Faça um programa que leia uma string
do usuário e conte quantas vogais (a, e, i, o, u)
existem na string. Imprima o número de vogais
'''
palavra = str(input('Digite a palavra: '))
numVogais = 0
for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        numVogais += 1
print(f'Número de vogais da palavra {palavra} é {numVogais} vogais')
