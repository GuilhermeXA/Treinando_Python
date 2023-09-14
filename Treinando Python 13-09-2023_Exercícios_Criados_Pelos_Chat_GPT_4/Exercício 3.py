'''
Exercício 3:
Crie um programa que leia uma lista de nomes
de pessoas e retorne uma lista com os nomes
em ordem alfabética.
'''
listaNomes = []
while True:
    nome = str(input('Digite um nome: '))
    if nome == '':
        break
    listaNomes.append(nome)

print(f'A lista digitada foi {listaNomes}')
listaNomes.sort()
print(f'A lista ordenada é {listaNomes}')
