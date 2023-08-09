# Lê o valor da idade em dias
idade_em_dias = int(input())

# Calcula os anos, meses e dias
anos = idade_em_dias // 365
idade_em_dias %= 365

meses = idade_em_dias // 30
dias = idade_em_dias % 30

# Imprime o resultado formatado
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
