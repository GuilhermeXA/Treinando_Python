# Dicionário que mapeia DDDs às cidades correspondentes
ddd_cidades = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

# Lê o número do DDD
ddd = int(input())

# Verifica se o DDD está no dicionário
if ddd in ddd_cidades:
    cidade = ddd_cidades[ddd]
    print(cidade)
else:
    print("DDD nao cadastrado")
