'''
Exercício 10: Faça um programa que leia uma lista de
nomes da entrada padrão e ordene-os em ordem alfabética.
'''
listaNomes = []
while True:
    nome = str(input('Digite um nome: '))
    if nome == 0 or nome == '':
        break
    listaNomes.append(nome)

print('Lista de nomes ', listaNomes)
listaNomes.sort()
print('Lista de nomes ordenada ', listaNomes)
