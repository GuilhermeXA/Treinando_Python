'''
Exercício 1: Soma dos Números Pares

Escreva um programa que calcule a soma de todos os
números pares de 1 a N, onde N é um número inteiro
positivo fornecido pelo usuário.
'''
repeticao = int(input('Digite a quantidade de números desejada: '))
listaPares = []
soma = 0
for i in range(0, repeticao):
    if i % 2 == 0:
        soma += i
        listaPares.append(i)
print(f'A lista dos números é {listaPares}')
print(f'A soma deles é {soma}')
