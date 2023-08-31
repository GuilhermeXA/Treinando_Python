# Número de casos de teste
n = int(input())

# Processar cada caso de teste
for _ in range(n):
    texto = input().split()
    mensagem_oculta = ''.join([palavra[0] for palavra in texto])
    print(mensagem_oculta)
