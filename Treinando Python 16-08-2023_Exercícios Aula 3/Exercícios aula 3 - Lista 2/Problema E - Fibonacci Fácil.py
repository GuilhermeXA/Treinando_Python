def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

num = int(input())
sequence = fibonacci(num)
print(' '.join(map(str, sequence)))
