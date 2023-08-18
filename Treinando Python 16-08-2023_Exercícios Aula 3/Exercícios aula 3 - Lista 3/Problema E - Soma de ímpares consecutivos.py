X = int(input())
Y = int(input())

# Certifica-se de que X seja sempre o menor valor
if X > Y:
    X, Y = Y, X

soma_impares = 0

# Loop para percorrer os números entre X e Y (exclusivo)
for num in range(X + 1, Y):
    if num % 2 != 0:  # Verifica se o número é ímpar
        soma_impares += num

print(soma_impares)
