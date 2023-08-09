vendedor = str(input())
salario = float(input())
valorVendas = float(input())
bonus = valorVendas * 0.15
salarioFinal = salario + bonus
print(f'Total = R$ {salarioFinal:.2f}')
