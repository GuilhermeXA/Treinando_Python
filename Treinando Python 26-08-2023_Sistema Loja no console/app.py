class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total


def main():
    print("Bem-vindo à Loja!")
    user_name = input("Digite seu nome: ")
    print("Produtos disponíveis:")
    products = [
        Product("Produto 1", 10),
        Product("Produto 2", 20),
        Product("Produto 3", 30),
        Product("Produto 4", 40),
        Product("Produto 5", 50)
    ]

    shopping_cart = ShoppingCart()

    while True:
        print("\nEscolha um produto para comprar:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.name} - R${product.price:.2f}")

        choice = int(input("Digite o número do produto (ou 0 para finalizar): "))

        if choice == 0:
            break

        if 1 <= choice <= len(products):
            selected_product = products[choice - 1]
            shopping_cart.add_item(selected_product)
            print(f"{selected_product.name} adicionado ao carrinho.")

    total_amount = shopping_cart.calculate_total()
    print(f"Total da compra: R${total_amount:.2f}")

    payment_method = input("Forma de pagamento (à vista ou cartão): ")
    if payment_method == "cartão":
        installments = int(input("Quantas parcelas? "))
        if installments <= 0:
            print("Número inválido de parcelas.")
        else:
            installment_amount = total_amount / installments
            print(f"Valor das parcelas: R${installment_amount:.2f}")
    else:
        print("Pagamento à vista.")

    print(f"\nObrigado pela compra, {user_name}! Volte sempre.")


if __name__ == "__main__":
    main()
