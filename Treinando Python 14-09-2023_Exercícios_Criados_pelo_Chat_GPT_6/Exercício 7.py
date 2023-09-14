'''
Desenvolva um programa que leia uma lista de palavras
e retorne a palavra mais longa e a palavra mais curta.
'''
listaPalavras = list()
maiorPalavra, menorPalavra = '', ''
while True:
    palavra = str(input('Digite um palavra: '))
    if palavra == 0 or palavra == '' or palavra == 'parar':
        break
    listaPalavras.append(palavra)

for i in listaPalavras:
    tamanho = len(i)
    if tamanho > len(maiorPalavra):
        maiorPalavra = i

menorPalavra = maiorPalavra
for j in listaPalavras:
    tamanho = len(j)
    if tamanho < len(menorPalavra):
        menorPalavra = j

print(f'A lista de palavras digitadas é {listaPalavras}')
print(f'A maior palavra digitada foi {maiorPalavra}')
print(f'A menor palavra digitada foi {menorPalavra}')
