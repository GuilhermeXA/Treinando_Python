# Lê o salário do funcionário
salario = float(input())

# Define a tabela de reajuste
tabela = [(0, 400, 15), (400.01, 800, 12), (800.01, 1200, 10), (1200.01, 2000, 7)]

# Inicializa as variáveis para armazenar o novo salário e o percentual de reajuste
novo_salario = salario
percentual_reajuste = 0

# Encontra o intervalo de reajuste correspondente ao salário
for inicio, fim, percentual in tabela:
    if inicio <= salario <= fim:
        percentual_reajuste = percentual
        novo_salario += (salario * percentual / 100)
        break

# Se o salário for maior que 2000, aplica o reajuste correspondente
if salario > 2000:
    percentual_reajuste = 4
    novo_salario += (salario * 4 / 100)

# Calcula o valor do reajuste
valor_reajuste = novo_salario - salario

# Imprime o novo salário, o valor do reajuste e o percentual de reajuste
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {valor_reajuste:.2f}")
print(f"Em percentual: {percentual_reajuste} %")
