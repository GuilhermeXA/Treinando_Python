'''
Exercício 5: Escreva um programa que leia
uma lista de números inteiros e imprima o
maior e o menor número da lista.
'''
listaDeNumeros = []
maior, menor = 0, 0
while True:
    numero = int(input('Digite um número: '))
    if numero <= 0 or numero == '':
        break
    listaDeNumeros.append(numero)

for i in listaDeNumeros:
    if i > maior:
        maior = i

menor = maior
for j in listaDeNumeros:
    if i < menor:
        menor = i

print(f'Lista de valores digitados é {listaDeNumeros}')
print(f'O Maior valor da lista é {maior}')
print(f'O Menor valor da lista é {menor}')
