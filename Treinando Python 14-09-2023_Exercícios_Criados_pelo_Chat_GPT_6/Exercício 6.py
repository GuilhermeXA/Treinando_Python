'''
Escreva um programa que leia uma lista de números
e retorne o maior e o menor número da lista.
'''
listaNumeros = []
maior, menor = 0, 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 0 or numero == '':
        break
    listaNumeros.append(numero)

for i in listaNumeros:
    if i > maior:
        maior = i

menor = maior
for j in listaNumeros:
    if j < menor:
        menor = j

print(f'A lista de números é {listaNumeros}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
