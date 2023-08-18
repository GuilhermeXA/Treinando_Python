rep = int(input())
valorIn, valorOut = 0, 0
for i in range(0, rep):
    num = int(input())
    if num >= 10 and num <= 20:
        valorIn += 1
    else:
        valorOut += 1

print(f'{valorIn} in')
print(f'{valorOut} out')
