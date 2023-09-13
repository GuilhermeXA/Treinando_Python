'''
Exercício 3: Escreva um programa que peça ao usuário
um número inteiro positivo e calcule o fatorial desse
número. O fatorial de um número é o produto de todos
os números inteiros positivos de 1 até o número dado.
'''
from math import factorial
numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {factorial(numero)}')
