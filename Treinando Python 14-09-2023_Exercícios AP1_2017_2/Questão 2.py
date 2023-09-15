def fatorial_duplo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_duplo(n - 2)


while True:
    n = int(input("Digite um número natural (ou -1 para sair): "))

    if n == -1:
        break

    if n % 2 == 0:
        print(f"O número {n} é par")
    else:
        resultado = fatorial_duplo(n)
        print(f"O fatorial duplo de {n} é {resultado}")
