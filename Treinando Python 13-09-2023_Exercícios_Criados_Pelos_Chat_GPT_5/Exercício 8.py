'''
Exercício 8: Escreva um programa que leia um
número inteiro da entrada padrão e calcule o
fatorial desse número.
'''
from math import factorial
numero = int(input('Digite um número: '))
print('O fatorial de {} é {}'.format(numero, factorial(numero)))
