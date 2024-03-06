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
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.product_price} Количество - {self.product_quantity}")


    @classmethod
    def create_product(cls, product_name, product_description, product_price, product_quantity):
        """
        создали новый товар в классе Products (объект)
        :param product_name:
        :param product_description:
        :param product_price:
        :param product_quantity:
        :return: new_product_object
        """
        new_product_object = cls(product_name, product_description, product_price, product_quantity)
        print("Создали новый продукт:", new_product_object)
        return new_product_object

    # @property
    # def get_category_products(self):
    #     return f'{self.product_name}, {self.product_price} руб. Остаток: {self.product_quantity} шт.'

# emp = Product('Iphone 5', "128GB, Gray space", 10000.0, 3)
# print(emp.get_category_products)

# new_product_object = Product.create_product('Iphone 5', "128GB, Gray space", 10000.0, 3)