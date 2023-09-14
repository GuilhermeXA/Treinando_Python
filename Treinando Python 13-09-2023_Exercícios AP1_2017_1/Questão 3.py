def padovan(n):
    if n < 3:
        return 1
    else:
        return padovan(n - 2) + padovan(n - 3)

# Processamento das entradas
while True:
    n = int(input("Digite um número natural (ou negativo para sair): "))
    if n < 0:
        break
    resultado = padovan(n)
    print(f"Termo {n} da sequência de Padovan: {resultado}")
