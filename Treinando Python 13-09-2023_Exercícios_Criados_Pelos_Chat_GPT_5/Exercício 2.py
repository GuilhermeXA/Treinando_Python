'''
Exercício 2: Escreva um programa que leia um número inteiro
da entrada padrão e determine se ele é par ou ímpar.
Em seguida, exiba uma mensagem correspondente.
'''
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')
