def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Lê o valor de N
n = int(input())

# Calcula o fatorial de N
fatorial = calcular_fatorial(n)

# Imprime o resultado
print(fatorial)
