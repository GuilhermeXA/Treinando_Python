def tempo_atendimento(N, M, tempos_funcionarios, itens_clientes):
    tempo_total = 0
    caixas = [0] * N  # Lista para armazenar o tempo de término de cada caixa

    for itens in itens_clientes:
        idx_caixa_livre = caixas.index(min(caixas))  # Encontrar o caixa livre mais rápido
        tempo_caixa_livre = caixas[idx_caixa_livre]

        tempo_atendimento_caixa = tempos_funcionarios[idx_caixa_livre] * itens
        tempo_total_caixa = max(tempo_caixa_livre, tempo_total) + tempo_atendimento_caixa

        caixas[idx_caixa_livre] = tempo_total_caixa
        tempo_total = tempo_total_caixa

    return tempo_total

def main():
    N, M = map(int, input().split())
    tempos_funcionarios = list(map(int, input().split()))
    itens_clientes = list(map(int, input().split()))

    resultado = tempo_atendimento(N, M, tempos_funcionarios, itens_clientes)
    print(resultado)

if __name__ == "__main__":
    main()
