# Função para calcular o número de alunos que não precisaram trocar de lugar
def contar_alunos_sem_troca(notas):
    # Criar uma lista de tuplas (nota, índice)
    alunos = list(enumerate(notas, start=1))

    # Ordenar a lista de alunos pela nota
    alunos_ordenados = sorted(alunos, key=lambda x: x[1], reverse=True)

    # Contar quantos alunos não precisaram trocar de lugar
    sem_troca = sum(1 for i, (_, indice) in enumerate(alunos_ordenados, start=1) if i == indice)

    return sem_troca

# Número de casos de teste
n = int(input())

# Processar cada caso de teste
for _ in range(n):
    # Número de alunos
    m = int(input())

    # Notas dos alunos
    notas = list(map(int, input().split()))

    # Calcular e imprimir o resultado
    resultado = contar_alunos_sem_troca(notas)
    print(resultado)
