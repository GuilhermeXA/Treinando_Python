# Leia 3 valores reais
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

# Verifique se os valores formam um triângulo
if A + B > C and A + C > B and B + C > A:
  # Os valores formam um triângulo
  # Calcule o perímetro do triângulo
  perimetro = A + B + C
  print("Perimetro = ", perimetro)
else:
  # Os valores não formam um triângulo
  # Calcule a área do trapézio que tem A e B como base e C como altura
  area = (A + B) * C / 2
  print("Area = ", area)
