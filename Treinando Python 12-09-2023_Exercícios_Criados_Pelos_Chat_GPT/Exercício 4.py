'''
Exercício 4: Crie um programa que gere uma lista de números
inteiros aleatórios no intervalo de 1 a 100 e encontre o
maior e o menor número na lista. Imprima esses valores.
'''
from random import randint
repeticao = int(input('Digite a quantidade de números: '))
listaNumeros = []
maiorValor, menorValor = 0,0
for i in range(1, repeticao):
    listaNumeros.append(randint(1,100))
for j in listaNumeros:
    if j > maiorValor:
        maiorValor = j
    elif j < menorValor or j > 0:
        menorValor = j
print(f'Lista de valores {listaNumeros}')
print(f'O menor valor é {menorValor} e o maior valor é {maiorValor}')
