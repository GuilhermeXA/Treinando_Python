'''
Exercício 9: Crie uma função que receba uma
lista de números inteiros como argumento e
retorne a média dos números na lista.
'''
listaInteiros = []
while True:
    numero = int(input('Digite o número: '))
    if numero == 0 or numero == '':
        break
    listaInteiros.append(numero)

soma, qtd = 0, 0
for i in listaInteiros:
    soma += i
    qtd += 1
media = soma / qtd

print(f'A lista de números é {listaInteiros}')
print(f'A média dos números da lista é {media}')
