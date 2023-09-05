valoresPermutacao = input("")
permutacao = list(map(int, valoresPermutacao.split()))

n = len(permutacao)
elementosPassados = [False] * n
ciclos = []

for i in range(n):
    if not elementosPassados[i]:
        ciclo = []
        j = i
        while not elementosPassados[j]:
            ciclo.append(j + 1)
            elementosPassados[j] = True
            j = permutacao[j] - 1

        if len(ciclo) > 1:
            ciclos.append(ciclo)

for ciclo in ciclos:
    textoCiclo = " ".join(map(str, ciclo))
    print("(", textoCiclo, ")", end=" ")
