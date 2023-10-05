def verificar_presenca_minima(n, nomes, registros):
    presenca_minima = 0.75 * n
    ausentes = []

    for nome, registro in zip(nomes, registros):
        presencas = registro.count('P')
        ausencias = registro.count('A')

        # Considera as ausências com atestado médico (M)
        presencas += registro.count('M')

        # Calcula a porcentagem de presença
        porcentagem_presenca = presencas / (presencas + ausencias)

        if porcentagem_presenca < 0.75:
            ausentes.append(nome)

    return ausentes

# Leitura da entrada
T = int(input())

for _ in range(T):
    N = int(input())
    nomes = input().split()
    registros = input().split()

    # Verifica os estudantes ausentes
    estudantes_ausentes = verificar_presenca_minima(N, nomes, registros)

    # Saída
    print(" ".join(estudantes_ausentes))
