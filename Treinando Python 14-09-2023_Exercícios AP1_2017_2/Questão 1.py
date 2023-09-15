# Função para verificar se uma string é palíndrome
def is_palindrome(s):
    return s == s[::-1]


# Inicialização das variáveis
strings_lidas = 0
palindromes = 0
palindromes_com_vogal = 0

# Loop para ler strings da entrada padrão
while True:
    entrada = input("Digite uma string (ou pressione Enter para sair): ")

    if entrada == "":
        break

    strings_lidas += 1

    if is_palindrome(entrada):
        palindromes += 1

        # Verificar se a string palíndrome contém pelo menos uma vogal
        if any(char.lower() in 'aeiou' for char in entrada):
            palindromes_com_vogal += 1

print(f"Quantidade de strings lidas: {strings_lidas}")
print(f"Quantidade de strings palíndromes: {palindromes}")
print(f"Quantidade de strings palíndromes com pelo menos uma vogal: {palindromes_com_vogal}")
