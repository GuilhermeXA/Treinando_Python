# Função para calcular o número de Fibonacci e contar as chamadas recursivas
def fibonacci(n, calls):
    calls[n] += 1

    if n <= 1:
        return n
    if fib_values[n] != -1:
        return fib_values[n]

    fib_values[n] = fibonacci(n - 1, calls) + fibonacci(n - 2, calls)
    return fib_values[n]


# Número máximo de casos de teste
MAX_CASES = 40

# Inicialização das estruturas de dados
fib_values = [-1] * MAX_CASES
calls = [0] * MAX_CASES

# Lê o número de casos de teste
N = int(input())

for _ in range(N):
    X = int(input())
    result = fibonacci(X, calls)

    print(f'fib({X}) = {calls[X] - 1} calls = {result}')
