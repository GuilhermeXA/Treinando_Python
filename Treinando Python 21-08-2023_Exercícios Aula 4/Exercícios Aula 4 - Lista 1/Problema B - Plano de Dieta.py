def dieta(jantar, cafe_da_manha, almoco):
    cafe_e_almoco = cafe_da_manha + almoco
    dieta_restante = [alimento for alimento in jantar if alimento not in cafe_e_almoco]

    if len(dieta_restante) == 0:
        return 'CHEATER'

    return ''.join(sorted(dieta_restante))

# Lê o número de casos de teste
n = int(input())

for _ in range(n):
    dieta_str = input()
    cafe_da_manha_str = input()
    almoco_str = input()

    resultado = dieta(dieta_str, cafe_da_manha_str, almoco_str)
    print(resultado)
