# Função para calcular as notas e moedas necessárias
def calcular_notas_moedas(valor):
    # Lista de notas e moedas disponíveis
    notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

    # Dicionário para armazenar a quantidade de cada nota/moeda
    quantidade_notas_moedas = {}

    # Iteração sobre as notas/moedas disponíveis
    for nota_moeda in notas_moedas:
        # Contagem da quantidade necessária de cada nota/moeda
        quantidade = int(valor / nota_moeda)
        valor -= quantidade * nota_moeda

        # Adicionando a quantidade no dicionário
        quantidade_notas_moedas[nota_moeda] = quantidade

    return quantidade_notas_moedas

# Leitura do valor de ponto flutuante
valor = float(input())

# Chamada da função para calcular notas e moedas
resultado = calcular_notas_moedas(valor)

# Saída formatada
print('NOTAS E MOEDAS:')
for nota_moeda, quantidade in resultado.items():
    print(f'{quantidade} nota(s) de R$ {nota_moeda:.2f}')
