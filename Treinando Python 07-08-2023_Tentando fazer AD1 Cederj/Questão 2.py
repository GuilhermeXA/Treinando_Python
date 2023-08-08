menor = float('inf')
maior = float('-inf')
listaNumeros = []
listaPares = []
listaImpares = []
somaListaPares = 0
somaListaImpares = 0
quantValoresListaPares = 0
quantValoresListaImpares = 0

while True:
    numero = input()
    if numero == '':
        break
    else:
        numero = int(numero)
        listaNumeros.append(numero)
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

for j in listaNumeros:
    if j % 2 == 0:
        listaPares.append(j)
        somaListaPares += j
        quantValoresListaPares += 1
    else:
        listaImpares.append(j)
        somaListaImpares += j
        quantValoresListaImpares += 1

mediaListaPares = somaListaPares / quantValoresListaPares
mediaListaImpares = somaListaImpares / quantValoresListaImpares

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Média dos Pares é {mediaListaPares:.2f}')
print(f'Média dos Ímpares é {mediaListaImpares:.1f}')
