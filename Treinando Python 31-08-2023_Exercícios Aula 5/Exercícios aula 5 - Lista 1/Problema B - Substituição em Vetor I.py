X = []
for _ in range(10):
    valor = int(input())
    if valor <= 0:
        X.append(1)
    else:
        X.append(valor)

for i in range(10):
    print(f"X[{i}] = {X[i]}")
