# Função para calcular a solução da sequência proposta por Paula
def calcular_solucao(digito1, letra, digito2):
    if letra.isupper():
        return int(digito2) - int(digito1)
    elif letra.islower():
        return int(digito1) + int(digito2)
    else:
        return int(digito1) * int(digito2)

# Lê o número de casos de teste
n = int(input())

# Processa cada caso de teste
for _ in range(n):
    sequencia = input()
    digito1, letra, digito2 = sequencia
    solucao = calcular_solucao(digito1, letra, digito2)
    print(solucao)
