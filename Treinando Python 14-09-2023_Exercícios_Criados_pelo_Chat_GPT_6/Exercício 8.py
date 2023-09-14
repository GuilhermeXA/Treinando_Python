'''
Faça um programa que leia um número e
determine se ele é primo.
'''
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

numero = int(input("Digite um número inteiro: "))

if is_prime(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
