# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo
hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final)

# Calcule a duração do jogo
duracao_em_minutos = (hora_final - hora_inicial) * 60 + (minuto_final - minuto_inicial)

# Imprima a mensagem com a duração do jogo
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_em_minutos // 60, duracao_em_minutos % 60))
