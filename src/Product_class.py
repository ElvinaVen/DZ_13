class Product:
    product_name: str
    product_description: str
    product_price: float
    product_quantity: int  # количество в наличии

    def __init__(self, product_name, product_description, product_price, product_quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_quantity = product_quantity

    def __repr__(self):
        return (f"Имя продукта - {self.product_name}\nОписание продукта - {self.product_description}\n"
                f"Стоимость продукта - {self.product_price}\nКоличество - {self.product_quantity}\n")
