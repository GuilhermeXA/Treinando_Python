L = int(input())
T = input()

M = []
for _ in range(12):
    row = []
    for _ in range(12):
        row.append(float(input()))
    M.append(row)

total = 0
count = 0
for i in range(12):
    total += M[L][i]
    count += 1

if T == 'M':
    total /= count

print(f"{total:.1f}")
