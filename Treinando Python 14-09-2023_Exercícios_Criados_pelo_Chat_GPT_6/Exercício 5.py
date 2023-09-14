'''
Crie um programa que peça ao usuário um número
e imprima a tabuada desse número até 10.
'''
numero = int(input('Digite um número inteiro: '))
for i in range(1, 11):
    print(f'{i} * {numero} = {i*numero}')
