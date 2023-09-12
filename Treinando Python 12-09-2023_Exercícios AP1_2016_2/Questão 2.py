# Função recursiva para converter um número decimal para outra base
def converte(numDecimal, base):
    if numDecimal == 0:
        return ""
    else:
        resto = numDecimal % base
        return converte(numDecimal // base, base) + str(resto)

# Programa principal
valores_decimal = []
valor = input("Digite um valor inteiro na base decimal (ou 'fim' para encerrar): ")

while valor != "fim":
    valor_decimal = int(valor)
    valores_decimal.append(valor_decimal)
    valor = input("Digite outro valor inteiro na base decimal (ou 'fim' para encerrar): ")

bases = [2, 3, 4, 5, 6, 7, 8, 9]

for valor_decimal in valores_decimal:
    resultados = [converte(valor_decimal, base) for base in bases]
    resultados_formatados = " ".join(resultados)
    print(resultados_formatados)
