# Lista para armazenar os números digitados
numeros = []

# Ler números até que um número negativo seja digitado
while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    numeros.append(num)

# Verificar quantos números foram lidos
quantidade = len(numeros)

if quantidade == 0:
    print("Nenhum valor válido!!!")
elif quantidade == 1:
    print(f"Apenas um valor foi lido: {numeros[0]}")
else:
    # Ordenar a lista em ordem decrescente
    numeros.sort(reverse=True)

    # Pegar os dois maiores números
    maior1 = numeros[0]
    maior2 = numeros[1]

    print(f"Os dois maiores números lidos foram: {maior1} e {maior2}")
