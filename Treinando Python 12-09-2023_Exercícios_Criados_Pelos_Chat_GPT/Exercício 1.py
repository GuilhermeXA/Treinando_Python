'''
Exercício 1: Crie um programa que peça ao usuário
para digitar um número inteiro e, em seguida,
verifique se o número é par ou ímpar.
Imprima uma mensagem indicando o resultado.
'''
numeroInteiro = int(input('Digite um número par: '))
if numeroInteiro % 2 == 0:
    print(f'{numeroInteiro} é par')
else:
    print(f'{numeroInteiro} é ímpar')
