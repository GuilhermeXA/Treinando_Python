'''
Exercício 2: Média de Idades

Crie um programa que peça ao usuário para inserir
as idades de um grupo de pessoas (até que ele digite
0 para sair). Ao final, o programa deve calcular e
imprimir a média das idades.
'''
listaIdades = []
soma, quantidade = 0,0
while True:
    idade = int(input('Digite uma idade: '))
    if idade == 0:
        break
    listaIdades.append(idade)
    soma += idade
    quantidade += 1
media = soma / quantidade
print(f'A lista de idades digitadas é {listaIdades}')
print(f'A média das idades é {media}')
