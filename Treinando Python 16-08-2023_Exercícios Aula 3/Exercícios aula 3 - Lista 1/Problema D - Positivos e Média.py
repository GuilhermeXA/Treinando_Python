somaNumerosPositivos = 0
numPositivos = 0
for a in range(0,6):
    num = float(input())
    if num > 0:
        somaNumerosPositivos += num
        numPositivos += 1

mediaPositivos = somaNumerosPositivos / numPositivos
print(f'{numPositivos} valores positivos')
print(f'{mediaPositivos:.1f}')
