# Programa Completo
# Subprogramas
def flip(n):
    print('Flip')
    if n>0:
        flop(n-1)
def flop(n):
    print('Flop')
    if n>0:
        flip(n-1)
# Programa Principal
flip(5)
