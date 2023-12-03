#Programa que cria arquivo de texto
with open('meuArquivo.txt', 'w') as arquivo:
    arquivo.write('Testando escrever no texto\n')
    arquivo.write('Escrevendo mais')
    conteudo = arquivo.read()
    print(conteudo)
