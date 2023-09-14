'''
Exercício 6: Crie um programa que leia uma lista
de números inteiros da entrada padrão e ordene-os
em ordem crescente.
'''
listaNumeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0 or numero == '':
        break
    listaNumeros.append(numero)

print(f'Lista de números digitados {listaNumeros}')
listaNumeros.sort()
print(f'Lista de números ordenada {listaNumeros}')
