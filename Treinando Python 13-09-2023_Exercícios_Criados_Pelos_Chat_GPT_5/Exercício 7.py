'''
Exercício 7: Implemente um jogo da forca em que o
jogador deve adivinhar uma palavra secreta. O jogo
deve mostrar a palavra com traços representando as
letras não adivinhadas e permitir que o jogador
insira letras para tentar adivinhar a palavra.
'''
import random

# Lista de palavras para o jogo
palavras = ["python", "javascript", "java", "ruby", "php", "csharp", "kotlin", "swift"]


# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)


# Função para inicializar a palavra secreta com traços
def inicializar_palavra(palavra):
    return ["_" for _ in palavra]


# Função para exibir a palavra atual
def exibir_palavra(palavra):
    return " ".join(palavra)


# Função para verificar se a letra está na palavra
def verificar_letra(palavra, palavra_secreta, letra):
    acerto = False
    for i in range(len(palavra)):
        if palavra[i] == letra:
            palavra_secreta[i] = letra
            acerto = True
    return acerto


# Função principal do jogo
def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    palavra_atual = inicializar_palavra(palavra_secreta)
    tentativas = 6  # Número de tentativas permitidas

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        print("\nPalavra atual:", exibir_palavra(palavra_atual))
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if letra in palavra_atual:
            print("Você já tentou essa letra antes.")
            continue

        if verificar_letra(palavra_secreta, palavra_atual, letra):
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")

        if "_" not in palavra_atual:
            print("\nParabéns! Você adivinhou a palavra:", "".join(palavra_secreta))
            break

    if "_" in palavra_atual:
        print("\nFim do jogo! A palavra secreta era:", "".join(palavra_secreta))


# Executa o jogo da forca
jogo_da_forca()
