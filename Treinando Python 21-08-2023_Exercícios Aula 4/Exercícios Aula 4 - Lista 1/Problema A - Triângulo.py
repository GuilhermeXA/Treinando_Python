def pode_formar_triangulo(a, b, c, d):
    # Função que verifica se é possível formar um triângulo
    return (a + b > d and a + c > d and b + c > d) or \
           (a + b > c and a + d > c and b + d > c) or \
           (a + c > b and a + d > b and c + d > b) or \
           (b + c > a and b + d > a and c + d > a)

# Lê os quatro valores da entrada
a, b, c, d = map(int, input().split())

# Verifica se é possível formar um triângulo e imprime o resultado
if pode_formar_triangulo(a, b, c, d):
    print('S')
else:
    print('N')
