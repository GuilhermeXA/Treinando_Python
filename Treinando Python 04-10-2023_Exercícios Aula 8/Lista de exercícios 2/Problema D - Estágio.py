def alunos_com_maior_media(codigos, medias):
    maior_media = max(medias)
    melhores_alunos = [codigo for codigo, media in zip(codigos, medias) if media == maior_media]
    return melhores_alunos

def main():
    turma = 1
    while True:
        N = int(input())
        if N == 0:
            break

        codigos = []
        medias = []

        for _ in range(N):
            codigo, media = map(int, input().split())
            codigos.append(codigo)
            medias.append(media)

        melhores_alunos = alunos_com_maior_media(codigos, medias)

        print(f'Turma {turma}')
        print(' '.join(map(str, melhores_alunos)))
        print()

        turma += 1

if __name__ == "__main__":
    main()
