'''
Exercício 4:
Escreva uma função que receba uma lista de números
inteiros e retorne uma nova lista contendo apenas
os números pares da lista original.
'''
listaInteiros = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 0 or numero == '':
        break
    listaInteiros.append(numero)

listaPares = []
for i in listaInteiros:
    if i % 2 == 0:
        listaPares.append(i)

print(f'Lista inicial {listaInteiros}')
print(f'Lista dos pares {listaPares}')
