'''
Crie um programa que converta uma temperatura em
graus Celsius para Fahrenheit. O usuário deve inserir
a temperatura em Celsius.
'''
tempCelsius = float(input('Digite a temperatura em célsius: '))
tempFahrenheit = (tempCelsius * 1.8) + 32
print('A temperatura {} em célsius equivale a temperatura {} em fahrenheit'.format(tempCelsius, tempFahrenheit))
