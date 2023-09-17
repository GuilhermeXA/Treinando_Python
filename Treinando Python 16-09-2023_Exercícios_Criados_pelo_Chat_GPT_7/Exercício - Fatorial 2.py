def fat(n):
    p = 1
    for ind in range(1,n+1):
        p = p * ind
    return p
