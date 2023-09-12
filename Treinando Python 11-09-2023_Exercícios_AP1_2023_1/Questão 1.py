# Função para verificar se um número é primo
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Lista para armazenar os números lidos
numeros = []

# Lê os números da entrada padrão
while True:
    entrada = input()
    if entrada == "":
        break
    numero = int(entrada)
    numeros.append(numero)

# Separa os números pares, ímpares e primos
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
primos = [num for num in numeros if is_prime(num)]

# Imprime os números pares
print("Números Pares:")
for num in pares:
    print(num)

# Imprime os números ímpares
print("\nNúmeros Ímpares:")
for num in impares:
    print(num)

# Imprime os números primos
print("\nNúmeros Primos:")
for num in primos:
    print(num)

# Mensagem de agradecimento
print("\nObrigado por utilizar nosso sistema!!!")
