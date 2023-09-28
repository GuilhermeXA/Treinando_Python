# Função para reordenar a fila e contar quantos alunos não trocaram de lugar
def reordenar_fila_e_contar(n, notas):
    # Cria uma lista de tuplas (nota, índice) para facilitar a ordenação
    alunos = [(nota, i) for i, nota in enumerate(notas)]

    # Ordena a lista de alunos pela nota em ordem decrescente
    alunos.sort(reverse=True)

    # Conta quantos alunos não trocaram de lugar
    nao_trocaram = sum(i == j for i, (_, j) in enumerate(alunos))

    return nao_trocaram

# Leitura do número de casos de teste
n = int(input())

# Lista para armazenar os resultados
resultados = []

# Loop para processar cada caso de teste
for _ in range(n):
    # Leitura do número de alunos e suas notas
    m = int(input())
    notas = list(map(int, input().split()))

    # Chama a função para reordenar a fila e contar os alunos que não trocaram de lugar
    resultado = reordenar_fila_e_contar(m, notas)

    # Adiciona o resultado à lista de resultados
    resultados.append(resultado)

# Imprime os resultados
for resultado in resultados:
    print(resultado)
