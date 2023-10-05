def classificar_frase(frase):
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    letras_presentes = set(frase.replace(" ", "").replace(",", ""))

    if letras_presentes == alfabeto:
        return "frase completa"
    elif len(letras_presentes) >= len(alfabeto) / 2:
        return "frase quase completa"
    else:
        return "frase mal elaborada"

# Leitura do número de casos de teste
N = int(input())

# Processamento de cada caso de teste
for _ in range(N):
    frase = input().lower()  # Converter para minúsculas para considerar maiúsculas e minúsculas iguais
    resultado = classificar_frase(frase)
    print(resultado)
