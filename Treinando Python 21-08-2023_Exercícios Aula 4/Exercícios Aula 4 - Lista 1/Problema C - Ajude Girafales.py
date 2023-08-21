def contar_diferencas(assinatura_original, assinatura_aula):
    # Função para contar as diferenças entre duas assinaturas
    count = 0
    for char_orig, char_aula in zip(assinatura_original, assinatura_aula):
        if char_orig != char_aula and char_orig.swapcase() != char_aula:
            count += 1
    return count

while True:
    n = int(input())
    if n == 0:
        break

    alunos = {}
    for _ in range(n):
        nome, assinatura_original = input().split()
        alunos[nome] = assinatura_original

    m = int(input())
    assinaturas_aula = {}
    for _ in range(m):
        nome, assinatura_aula = input().split()
        assinaturas_aula[nome] = assinatura_aula

    assinaturas_falsas = 0
    for aluno, assinatura_aula in assinaturas_aula.items():
        assinatura_original = alunos[aluno]
        diferenca = contar_diferencas(assinatura_original, assinatura_aula)
        if diferenca > 1:
            assinaturas_falsas += 1

    print(assinaturas_falsas)
