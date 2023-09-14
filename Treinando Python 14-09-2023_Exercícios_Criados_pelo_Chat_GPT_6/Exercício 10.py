'''
Crie um programa que leia uma lista de números
e retorne a média dos números na lista.
'''
listaNum = []
soma, qtd, media = 0, 0, 0
while True:
    numero = float(input('Digite um número: '))
    if numero == '' or numero == 0:
        break
    listaNum.append(numero)

for i in listaNum:
    soma += i
    qtd += 1

media = soma / qtd
print(f'A lista dos valores digitados é {listaNum}')
print(f'A média dos valores digitados é {media}')
