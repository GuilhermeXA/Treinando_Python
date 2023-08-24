import requests


class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://economia.awesomeapi.com.br/last/{self.api_key}/"

    def get_exchange_rates(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def convert_currency(self, from_currency, to_currency, amount):
        exchange_rates = self.get_exchange_rates()
        if not exchange_rates:
            return None

        from_to = f"{from_currency}_{to_currency}"
        if from_to not in exchange_rates:
            return None

        rate = exchange_rates[from_to]['bid']

        converted_amount = amount * rate
        return converted_amount


def main():
    api_key = "YOUR_AWESOMEAPI_KEY"  # Substitua pela sua chave da AwesomeAPI
    converter = CurrencyConverter(api_key)

    from_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    to_currency = input("Digite a moeda de destino (ex: BRL): ").upper()
    amount = float(input("Digite a quantidade: "))

    converted_amount = converter.convert_currency(from_currency, to_currency, amount)
    if converted_amount is None:
        print("Não foi possível realizar a conversão.")
    else:
        print(f"{amount} {from_currency} é igual a {converted_amount:.2f} {to_currency}")


if __name__ == "__main__":
    main()
