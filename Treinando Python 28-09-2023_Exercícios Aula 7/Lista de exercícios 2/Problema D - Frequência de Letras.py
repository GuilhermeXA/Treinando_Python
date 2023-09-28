from collections import Counter


def letras_mais_frequentes(texto):
    # Convertendo o texto para minúsculas e contando as letras
    contagem = Counter(texto.lower())

    # Encontrando a(s) letra(s) mais frequente(s)
    max_ocorrencias = max(contagem.values())
    letras_mais_frequentes = [letra for letra, ocorrencias in contagem.items() if ocorrencias == max_ocorrencias]

    # Ordenando as letras em ordem alfabética
    letras_mais_frequentes.sort()

    return letras_mais_frequentes


# Lendo o número de casos de teste
num_casos = int(input())

# Loop pelos casos de teste
for _ in range(num_casos):
    # Lendo a linha de texto
    linha = input().strip()

    # Chamando a função e imprimindo o resultado
    resultado = letras_mais_frequentes(linha)
    print(''.join(resultado))
