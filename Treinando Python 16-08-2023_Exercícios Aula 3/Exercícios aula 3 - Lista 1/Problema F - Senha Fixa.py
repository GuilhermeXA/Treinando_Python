senhaCorreta = 2002
while True:
    senhaTestada = int(input())
    if senhaTestada == senhaCorreta:
        print('Acesso permitido!')
        break
    else:
        print('Senha Inválida!')
