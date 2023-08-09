tempo_gasto = int(input())
velocidade_media = int(input())

distancia = tempo_gasto * velocidade_media
litros_necessarios = distancia / 12

print(f"{litros_necessarios:.3f}")
