# Lê o número inteiro N
N = int(input("Digite um número inteiro: "))

# Percorre todos os números de 1 a N e verifica se são divisores de N
print("Divisores de", N, ":")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
