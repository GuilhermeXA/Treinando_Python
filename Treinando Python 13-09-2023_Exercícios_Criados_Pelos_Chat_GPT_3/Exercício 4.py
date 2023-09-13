'''
Exercício 4: Crie uma função chamada verifica_primo
que recebe um número inteiro como argumento e verifica
se ele é um número primo. A função deve retornar True
se o número for primo e False caso contrário.
'''
def verifica_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Se for divisível por algum número, não é primo

    return True  # Se não for divisível por nenhum número, é primo

# Solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para verificar se é primo e imprime o resultado
if verifica_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
