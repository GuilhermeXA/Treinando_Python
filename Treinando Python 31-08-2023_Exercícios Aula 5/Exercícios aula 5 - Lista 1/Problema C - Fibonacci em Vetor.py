def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

T = int(input("Digite o número de casos de teste: "))

for _ in range(T):
    N = int(input())
    result = fibonacci(N)
    print(f"Fib({N}) = {result}")
