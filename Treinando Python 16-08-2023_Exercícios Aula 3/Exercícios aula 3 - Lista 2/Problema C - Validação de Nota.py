soma = 0
acumulador = 0
while True:
    num = float(input())
    if num >= 0 and num <= 10:
        soma += num
        acumulador += 1
        if acumulador == 2:
            break
    else:
        print('nota invalida')

media = soma / 2
print(f'media = {media:.2f}')
