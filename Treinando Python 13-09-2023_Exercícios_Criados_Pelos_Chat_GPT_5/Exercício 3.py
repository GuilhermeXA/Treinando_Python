'''
Exercício 3: Crie uma função que receba uma lista de números
inteiros como argumento e retorne o maior número da lista.
'''
listaNumeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0 or numero == '':
        break
    listaNumeros.append(numero)

maior, menor = 0, 0
for i in listaNumeros:
    if i > maior:
        maior = i

menor = maior
for j in listaNumeros:
    if j < menor:
        menor = i

print(f'Os valores da lista são {listaNumeros}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
