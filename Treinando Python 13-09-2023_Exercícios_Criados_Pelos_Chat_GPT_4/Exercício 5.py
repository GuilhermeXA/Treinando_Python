'''
Exercício 5:
Crie um programa que leia uma lista de números inteiros
e retorne a soma de todos os números primos da lista.
'''
def main():
    numeros = []  # Inicializa uma lista vazia para armazenar os números inteiros

    # Solicita ao usuário que insira números até que ele insira uma string vazia
    while True:
        entrada = input("Digite um número inteiro (ou deixe em branco para encerrar): ")
        if entrada == "":
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Função para verificar se um número é primo
    def eh_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Calcula a soma dos números primos na lista
    soma_primos = sum(num for num in numeros if eh_primo(num))

    # Exibe a soma dos números primos
    print("\nSoma dos números primos na lista:", soma_primos)

if __name__ == "__main__":
    main()
