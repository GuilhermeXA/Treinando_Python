'''
Exercício 2: Escreva um programa que solicite ao usuário
uma lista de números inteiros separados por vírgulas.
Em seguida, crie uma nova lista que contenha apenas os
números pares da lista original e imprima essa nova lista.
'''
listaNumeros = []
listaNumerosPares = []
repeticao = int(input('Digite o número total de valores que deseja digitar: '))
for i in range(0, repeticao):
    listaNumeros.append(int(input('Digite os números: ')))
for j in listaNumeros:
    if j % 2 == 0:
        listaNumerosPares.append(j)
print(f'Lista de números digitados geral: {listaNumeros}')
print(f'Lista de números que são pares: {listaNumerosPares}')
