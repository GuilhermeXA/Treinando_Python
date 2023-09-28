def dieta(jantar, cafe_manha, almoco):
    # Concatenando as strings de café da manhã e almoço
    dieta_comida = cafe_manha + almoco

    # Verificando se a dieta está sendo seguida corretamente
    for comida in jantar:
        if comida not in dieta_comida:
            return "CHEATER"
        # Removendo a comida da dieta para evitar repetições
        dieta_comida = dieta_comida.replace(comida, '', 1)

    # Ordenando e retornando a dieta para o jantar
    return ''.join(sorted(dieta_comida))


# Lendo o número de casos de teste
num_casos = int(input())

# Loop pelos casos de teste
for _ in range(num_casos):
    # Lendo as strings de dieta, café da manhã e almoço
    dieta_str = input().strip()
    cafe_manha_str = input().strip()
    almoco_str = input().strip()

    # Chamando a função dieta e imprimindo o resultado
    resultado = dieta(dieta_str, cafe_manha_str, almoco_str)
    print(resultado)
