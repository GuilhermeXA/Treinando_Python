'''
Exercício 2:
Escreva uma função que recebe uma lista de números
e retorna a média aritmética dos valores.
'''
def media(listaNumeros):
    soma, qtd = 0, 0
    for i in listaNumeros:
        soma += i
        qtd += 1
    media = soma / qtd
    return media

listaDeNumeros = []
while True:
    numero = float(input('Digite um número: '))
    if numero <= 0 or numero == '':
        break
    listaDeNumeros.append(numero)

print(f'Os valores digitados são {listaDeNumeros}')
print(f'A média dos valores digitados é {media(listaDeNumeros)}')
