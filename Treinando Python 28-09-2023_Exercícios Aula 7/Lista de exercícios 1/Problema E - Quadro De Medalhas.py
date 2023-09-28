# Função para ordenar os países conforme as regras especificadas
def ordenar_quadro_medalhas(paises):
    return sorted(paises, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

# Número de países participantes
n = int(input())

# Lista para armazenar informações de cada país
paises = []

# Ler informações de cada país
for _ in range(n):
    nome, ouro, prata, bronze = input().split()
    ouro, prata, bronze = int(ouro), int(prata), int(bronze)
    paises.append((nome, ouro, prata, bronze))

# Ordenar o quadro de medalhas
quadro_ordenado = ordenar_quadro_medalhas(paises)

# Imprimir o resultado
for pais, ouro, prata, bronze in quadro_ordenado:
    print(f"{pais} {ouro} {prata} {bronze}")
