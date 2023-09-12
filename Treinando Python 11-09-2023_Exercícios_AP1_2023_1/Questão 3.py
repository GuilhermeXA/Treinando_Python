# Função de Collatz
def collatz(n):
    if not isinstance(n, int):
        return f"Valor {n} não é inteiro"
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

# Parte (a): Calcular a sequência de Collatz para um número dado
valor_xyz = input("Digite um número inteiro para calcular a sequência de Collatz: ")
try:
    valor_xyz = int(valor_xyz)
    resultado_a = collatz(valor_xyz)
    print(resultado_a)
except ValueError:
    print(f"Valor {valor_xyz} não é inteiro")

# Parte (b): Calcular a sequência de Collatz para o valor 7
resultado_b = collatz(7)
print("Sequência de Collatz para 7:")
print(resultado_b)

# Parte (c): Calcular a sequência de Collatz para todos os naturais de 3 até valor_xyz
if isinstance(valor_xyz, int):
    for i in range(3, valor_xyz + 1):
        resultado_c = collatz(i)
        print(f"Sequência de Collatz para {i}:")
        print(resultado_c)
