num = int(input())
valorIn, valorOut = 0, 0
for i in range(0, num):
    numero = int(input())
    if numero >= 10 and numero <= 20:
        valorIn += 1
    else:
        valorOut += 1

print(f'{valorIn} In')
print(f'{valorOut} Out')
