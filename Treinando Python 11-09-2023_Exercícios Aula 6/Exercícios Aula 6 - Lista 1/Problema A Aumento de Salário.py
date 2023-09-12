salario = float(input())
if salario <= 400:
    percentualReajuste = 15
elif salario <= 800:
    percentualReajuste = 12
elif salario <= 1200:
    percentualReajuste = 10
elif salario <= 2000:
    percentualReajuste = 7
elif salario > 2000:
    percentualReajuste = 4
valorReajuste = (salario / 100) * percentualReajuste
novoSalario = salario + valorReajuste
print(f'Novo salário: {novoSalario:.2f}')
print(f'Reajuste ganho: {valorReajuste:2f}')
print(f'Em percentual: {percentualReajuste}%')
