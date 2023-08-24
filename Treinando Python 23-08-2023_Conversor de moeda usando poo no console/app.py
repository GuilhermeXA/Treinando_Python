class Calculadora:
    def __init__(self):
        self.taxas = {'dolar': 5.23, 'euro': 6.17, 'libra': 7.12}

    def converter_para_real(self, moeda, quantidade):
        if moeda in self.taxas:
            taxa = self.taxas[moeda]
            resultado = quantidade * taxa
            return resultado
        else:
            return "Moeda não suportada"


def main():
    calculadora = Calculadora()

    print("Bem-vindo ao Conversor de Moedas!")
    moeda = input("Digite o nome da moeda (dolar, euro ou libra): ").lower()
    quantidade = float(input("Digite a quantidade da moeda: "))

    resultado = calculadora.converter_para_real(moeda, quantidade)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{quantidade} {moeda} é igual a {resultado:.2f} reais.")


if __name__ == "__main__":
    main()
