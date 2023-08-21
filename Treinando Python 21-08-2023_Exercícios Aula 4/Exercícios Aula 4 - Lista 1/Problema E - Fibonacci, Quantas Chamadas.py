# Usando programação dinâmica para calcular a sequência de Fibonacci
def fib(n, memo):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# Função para contar o número de chamadas recursivas
def count_calls(n, memo):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = count_calls(n - 1, memo) + count_calls(n - 2, memo) + 1
    return memo[n]


# Lê o número de casos de teste
num_cases = int(input())

for _ in range(num_cases):
    n = int(input())
    memo = {}
    result = fib(n, memo)
    num_calls = count_calls(n, memo)
    print(f"fib({n}) = {num_calls} calls = {result}")
