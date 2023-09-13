'''
Exercício 2: Crie uma função chamada soma_lista
que recebe uma lista de números como argumento
e retorna a soma de todos os números na lista.
'''
def soma_lista(listaNumeros):
    soma = 0
    for i in listaNumeros:
        soma += i
    return print(f'A soma da lista {listaNumeros} é {soma}')

listaDeNumeros = []
while True:
    listaDeNumeros.append(int(input('Digite um número inteiro: ')))
    opcao = str(input('Quer continuar? (s/n) '))
    if opcao != 's':
        break

#Chamando a função
soma_lista(listaDeNumeros)
