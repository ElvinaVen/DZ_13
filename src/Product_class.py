class Product:
    product_name: str
    product_description: str
    product_price: float
    product_quantity: int  # количество в наличии

    def __init__(self, product_name, product_description, product_price, product_quantity):

        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.product_price} Количество - {self.product_quantity}")

    @property
    def price(self):
        return self.product_price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            self.product_price = new_price
            print("цена корректная")

    @staticmethod
    def my_decorator(func):
        def inner(**kwargs):
            result = func(**kwargs)
            result2 = {
                "name": result.product_name,
                "description": result.product_description,
                'price': result.product_price,
                'quantity': result.product_quantity
            }
            print(f"7) Создали новый экземпляр товара = {result2}")
            return result2
        return inner

    @staticmethod
    @my_decorator
    def create_new_product_object(**kwargs):
        """
        создали новый экземпляр класса Product
        """
        new_product_object = Product(**kwargs)
        # print(new_product_object)
        return new_product_object
