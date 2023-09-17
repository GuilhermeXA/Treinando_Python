qtdLetras = 0
listaPalavras = []
while True:
    palavra = str(input())
    if palavra == "":
        break
    listaPalavras.append(palavra)

listaNumLetras = dict()
for i in listaPalavras:
    qtdLetras = len(i)
    #listaNumLetras[f'{i}']
    listaNumLetras[f'{i}'] = qtdLetras
    qtdLetras = 0

for j, k in listaNumLetras.items():
    print(f'A palavra {j} tem {k} letras')
