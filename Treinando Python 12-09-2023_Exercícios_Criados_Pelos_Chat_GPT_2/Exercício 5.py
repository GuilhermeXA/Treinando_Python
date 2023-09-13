'''
Exercício 5: Conversor de Moedas

Crie um programa que converta uma quantia em reais
para dólares. O programa deve pedir ao usuário a taxa
de câmbio atual e a quantidade de reais a serem convertidos.
'''
valorEmReal = float(input('Digite o valor em reais: '))
taxaDeCambio = float(input('Digite a taxa de câmbio: '))
valorEmDolar = valorEmReal / taxaDeCambio
print(f'O valor em real R${valorEmReal:.2f} convertido a uma taxa de {taxaDeCambio:2f}% em dólar é U${valorEmDolar:2f}')
