# Leitura dos valores de ponto flutuante
a, b, c = map(float, input().split())

# Ordena os valores em ordem decrescente
valores_ordenados = sorted([a, b, c], reverse=True)

# Atribui os valores ordenados às variáveis a, b e c
a, b, c = valores_ordenados

# Verifica o tipo de triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")
