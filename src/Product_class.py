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
        # product_object = Product(product_name, product_description, product_price, product_quantity)
        return cls(product_name, product_description, product_price, product_quantity)

    @staticmethod
    def add_product_object_in_prod_list(prod_list, product_object):
        """
        Создаем список всех товаров

        :param prod_list:
        :param product_object:
        :return: prod_list
        """

        prod_list.append(product_object)
        return prod_list  # список всех категорий

    # @classmethod
    # def get_product_list(cls):
    #     return cls.prod_list

    # @classmethod
    # def add_in_category(cls, prod):
    #     return Category.set_product(prod)

    # @classmethod
    # def create_new_product_object(cls, product_name, product_description, product_price, product_quantity):
    #     """
    #     создали новый экземпляр класса Product
    #     """
    #     return cls(product_name, product_description, product_price, product_quantity)

    # def my_decorator(func):
    #     def inner(**kwargs):
    #         pass
    #     return inner
    #
    # def create_new_product_object(product_name, product_description, product_price, product_quantity):
    #     """
    #     создали новый экземпляр класса Product
    #     """
    #     a = {'name': 'Samsung', 'description': 'Серый цвет', 'price': 18.0, 'quantity': 111}
    #     return a

    # new_f = my_decorator(create_new_product_object)
    # params = {'product_name': 'Iphone 5',"product_description": "128GB Gray space","product_price": 10000.0, "product_quantity": 3}
    # # e = new_f(product_name ='Iphone 5',product_description="128GB Gray space",product_price=10000.0, product_quantity= 3)
    # e = new_f(**params)
    # print(e)

    @property
    def product_price_func(self):
        return self.product_price

    @product_price_func.setter
    def product_price_func(self, product_price):
        if product_price <= 0:
            print("цена введена некорректная")
        else:
            self.product_price = product_price
            print("цена корректная")

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

    @staticmethod
    def my_decorator(func):
        def inner(**kwargs):
            result = func(**kwargs)
            print(f"7) Создали новый экземпляр товара = {result}")
            return result
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
