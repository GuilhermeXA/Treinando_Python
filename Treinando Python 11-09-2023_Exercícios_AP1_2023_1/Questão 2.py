import math


# Função para calcular a distância entre dois pontos
def distancia_entre_pontos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Função para verificar se um ponto está dentro da circunferência
def ponto_dentro_da_circunferencia(x_ponto, y_ponto, x_circunferencia, y_circunferencia, raio_circunferencia):
    distancia = distancia_entre_pontos(x_ponto, y_ponto, x_circunferencia, y_circunferencia)
    return distancia <= raio_circunferencia


# Lista para armazenar os pontos
pontos = []

# Lê a quantidade de pontos
quantidade_pontos = int(input("Digite a quantidade de pontos: "))

# Lê os pontos da entrada padrão
for _ in range(quantidade_pontos):
    x_ponto, y_ponto = map(float, input("Digite as coordenadas do ponto (x y): ").split())
    pontos.append((x_ponto, y_ponto))

# Entra em um ciclo repetitivo para ler as circunferências
while True:
    x_circunferencia, y_circunferencia, raio_circunferencia = map(float, input(
        "Digite as coordenadas e o raio da circunferência (x y raio): ").split())

    # Verifica se a circunferência é nula (0, 0, 0)
    if x_circunferencia == 0 and y_circunferencia == 0 and raio_circunferencia == 0:
        break

    # Lista para armazenar os pontos dentro da circunferência
    pontos_dentro = []

    # Verifica quais pontos estão dentro da circunferência
    for x_ponto, y_ponto in pontos:
        if ponto_dentro_da_circunferencia(x_ponto, y_ponto, x_circunferencia, y_circunferencia, raio_circunferencia):
            pontos_dentro.append((x_ponto, y_ponto))

    # Imprime os pontos dentro da circunferência
    print("Pontos dentro da circunferência:")
    for x, y in pontos_dentro:
        print(f"({x}, {y})")

# Mensagem de agradecimento
print("\nObrigado por utilizar nosso sistema!!!")
