'''
Exercício 5: Escreva um programa que leia
uma lista de nomes de pessoas e, em seguida,
ordene a lista em ordem alfabética e a imprima.
'''
repeticao = int(input('Digite quantas palavras você deseja digitar: '))
listaNomes = []
for i in range(0, repeticao):
    listaNomes.append(str(input('Digite um nome: ').lower()))
print(f'Lista como foi digitada {listaNomes}')
listaNomes.sort()
print(f'Lista anterior ordenada:')
for j in listaNomes:
    print(j)
