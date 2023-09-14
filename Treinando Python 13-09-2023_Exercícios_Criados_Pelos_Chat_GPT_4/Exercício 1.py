'''
Exercício 1:
Crie um programa que receba uma lista de números inteiros
e retorne o maior e o menor número da lista.
'''
listaNumeros = []
maior, menor = 0, 0
while True:
    numero = int(input('Digite um número: '))
    if numero <= 0 or numero == '':
        break
    listaNumeros.append(numero)

for i in listaNumeros:
    if i > maior:
        maior = i

menor = maior
for j in listaNumeros:
    if i < menor:
        menor = i

print(f'Os valores digitados são {listaNumeros}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
