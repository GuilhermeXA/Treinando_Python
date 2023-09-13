'''
Exercício 4: Verificador de Palíndromos

Faça um programa que verifica se uma palavra ou
frase fornecida pelo usuário é um palíndromo,
ou seja, se ela é igual quando lida da esquerda
para a direita e vice-versa.
'''
palavra = str(input('Digite a palavra: '))
if palavra == palavra[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
