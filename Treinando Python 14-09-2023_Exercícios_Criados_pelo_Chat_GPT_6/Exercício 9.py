'''
Escreva um programa que leia uma lista de números
e retorne a soma de todos os números pares na lista.
'''
listaNum = list()
listaPares = []
soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == '' or numero == 0:
        break
    listaNum.append(numero)

for i in listaNum:
    if i % 2 == 0:
        soma += i
        listaPares.append(i)

print(f'A lista de valores digitados é {listaNum}')
print(f'A lista dos valores pares é {listaPares}')
print(f'A soma da lista dos valores pares é {soma}')
