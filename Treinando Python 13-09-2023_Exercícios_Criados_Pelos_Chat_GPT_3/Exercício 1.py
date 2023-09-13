'''
Exercício 1: Escreva um programa que solicite
ao usuário um número e determine se ele é par
ou ímpar. Em seguida, imprima uma mensagem
indicando o resultado.
'''
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número: {numero} é ímpar')
