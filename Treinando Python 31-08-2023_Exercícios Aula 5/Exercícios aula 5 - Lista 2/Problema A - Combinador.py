# Função para combinar duas strings
def combinar_strings(s1, s2):
    resultado = ''
    min_length = min(len(s1), len(s2))

    for i in range(min_length):
        resultado += s1[i] + s2[i]

    # Adicionar o restante da string mais longa
    if len(s1) > len(s2):
        resultado += s1[min_length:]
    else:
        resultado += s2[min_length:]

    return resultado


# Número de casos de teste
n = int(input())

# Processar cada caso de teste
for _ in range(n):
    s1, s2 = input().split()
    resultado = combinar_strings(s1, s2)
    print(resultado)
