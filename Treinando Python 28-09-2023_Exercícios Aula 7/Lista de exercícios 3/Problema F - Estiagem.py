def calcula_consumo_medio(pessoas_consumo):
    total_pessoas = 0
    total_consumo = 0

    for pessoas, consumo in pessoas_consumo:
        total_pessoas += pessoas
        total_consumo += consumo

    consumo_medio = total_consumo / total_pessoas

    return consumo_medio


def main():
    cidade_numero = 1

    while True:
        n = int(input())

        if n == 0:
            break

        pessoas_consumo = []

        for _ in range(n):
            x, y = map(int, input().split())
            pessoas_consumo.append((x, y))

        pessoas_consumo.sort(key=lambda item: item[1])

        print(f'Cidade# {cidade_numero}:')

        for pessoas, consumo in pessoas_consumo:
            print(f'{pessoas}-{consumo}')

        consumo_medio = calcula_consumo_medio(pessoas_consumo)
        print(f'Consumo medio: {consumo_medio:.2f}\n')

        cidade_numero += 1


if __name__ == "__main__":
    main()
