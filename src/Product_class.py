class Product:
    product_name: str
    product_description: str
    __product_price: float
    product_quantity: int  # количество в наличии

    def __init__(self, product_name, product_description, product_price, product_quantity):

        self.product_name = product_name
        self.product_description = product_description
        self.__product_price = product_price
        self.product_quantity = product_quantity

    def __repr__(self):
        return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
                f"Стоимость продукта - {self.__product_price} Количество - {self.product_quantity}")

    @property
    def price(self):
        return self.__product_price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("цена введена некорректная")
        else:
            self.__product_price = new_price
            print("цена корректная")

    @staticmethod
    def my_decorator(func):
        def inner(*args, **kwargs):
            result2 = {
                "name": kwargs['product_name'],
                "description": kwargs['product_description'],
                'price': kwargs['product_price'],
                'quantity': kwargs['product_quantity']
            }
            print(f"7) Создали новый экземпляр товара = {result2}")
            return result2
        return inner

    @classmethod
    @my_decorator
    def create_new_product_object(cls, **kwargs):
        """
        создали новый экземпляр класса Product
        """
        product_name = kwargs['product_name']
        product_description = kwargs['product_description']
        product_price = kwargs['product_price']
        product_quantity = kwargs['product_quantity']
        return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def create_product_object(cls, one_product_dict):
        """
        Создаем экземпляры класса Product
        :param one_product_dict
        :return: product_object
        """
        product_name = cls.get_product_name(one_product_dict)
        product_description = cls.get_product_description(one_product_dict)
        product_price = cls.get_product_price(one_product_dict)
        product_quantity = cls.get_quantity(one_product_dict)
        return cls(product_name, product_description, product_price, product_quantity)

    @staticmethod
    def get_product_name(products_list):
        """
        получаем наименование продукта для класса Products.
        :param products_list:
        :return:product_name
        """
        product_name = products_list['name']
        return product_name

    @staticmethod
    def get_product_description(products_list):
        """
        получаем описание продукта.
        :param products_list:
        :return:products_description
        """
        products_description = products_list['description']
        return products_description

    @staticmethod
    def get_product_price(products_list):
        """
        получаем цену продукта.
        :param products_list:
        :return:product_price
        """
        product_price = products_list['price']
        return product_price

    @staticmethod
    def get_quantity(products_list):
        """
        получаем количество на складе.
        :param products_list:
        :return:product_quantity
        """
        product_quantity = products_list['quantity']
        return product_quantity
