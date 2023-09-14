'''
Exercício 4: Faça um programa que leia uma string da
entrada padrão e conte quantas vogais (a, e, i, o, u)
estão presentes na string.
'''
vogaisA = 0
vogaisE = 0
vogaisI = 0
vogaisO = 0
vogaisU = 0
nome = str(input('Digite uma frase: '))
nome.lower()
for i in nome:
    if i == 'a':
        vogaisA += 1
    elif i == 'e':
        vogaisE += 1
    elif i == 'i':
        vogaisI += 1
    elif i == 'o':
        vogaisO += 1
    elif i == 'U':
        vogaisU += 1
print(f'Na frase {nome} tem: ')
print(f'{vogaisA} letras a')
print(f'{vogaisE} letras e')
print(f'{vogaisI} letras i')
print(f'{vogaisO} letras o')
print(f'{vogaisU} letras u')
