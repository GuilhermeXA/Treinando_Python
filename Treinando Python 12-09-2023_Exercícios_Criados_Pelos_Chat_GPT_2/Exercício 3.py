'''
Exercício 3: Fatorial

Desenvolva uma função em Python que calcule o fatorial
de um número inteiro N fornecido pelo usuário.
O fatorial de um número é o produto de todos os
inteiros positivos de 1 a N.
'''
from math import factorial
def fatorial(numero):
    return print(f'O fatorial de {numero} é {factorial(numero)}')

fatorial(int(input('Digite um número inteiro: ')))
