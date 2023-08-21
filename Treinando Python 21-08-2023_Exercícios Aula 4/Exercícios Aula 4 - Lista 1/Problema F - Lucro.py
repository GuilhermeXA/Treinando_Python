def calcular_lucro_maximo(dias, custo_por_dia, receitas):
    lucro_maximo = 0

    for i in range(dias):
        lucro_dia = 0
        for j in range(i, dias):
            lucro_dia += receitas[j] - custo_por_dia
            lucro_maximo = max(lucro_maximo, lucro_dia)

    return lucro_maximo


while True:
    try:
        dias = int(input())
        custo_por_dia = int(input())

        receitas = []
        for _ in range(dias):
            receita = int(input())
            receitas.append(receita)

        lucro_maximo = calcular_lucro_maximo(dias, custo_por_dia, receitas)
        print(lucro_maximo)
    except EOFError:
        break
