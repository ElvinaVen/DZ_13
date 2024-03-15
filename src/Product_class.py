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
        return f"Экз-р продукта - {self.product_name}, {self.product_description}, {self.__product_price}, {self.product_quantity}"

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
        def inner(**kwargs):
            result2 = {
                "name": kwargs['product_name'],
                "description": kwargs['product_description'],
                'price': kwargs['product_price'],
                'quantity': kwargs['product_quantity']
            }
            print(f"7) Создали новый экземпляр товара = {result2}")
            return result2

        return inner

    # @classmethod
    # @my_decorator
    # def create_new_product_object(cls, **kwargs):
    #     """
    #     создали новый экземпляр класса Product
    #     """
    #     product_name = kwargs['product_name']
    #     product_description = kwargs['product_description']
    #     product_price = kwargs['product_price']
    #     product_quantity = kwargs['product_quantity']
    #     return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def get_product_object(cls, src_file):
        """
        Создаем экземпляры класса Product
        :param one_category_list
        :return: product_object
        """
        product_name = cls.get_product_name(src_file)
        product_description = cls.get_product_description(src_file)
        product_price = cls.get_product_price(src_file)
        product_quantity = cls.get_product_quantity(src_file)
        return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def create_new_product_object(cls, product_name, product_description, product_price, product_quantity):
        """
        Создаем экземпляры класса Product
        :param product_quantity:
        :param product_price:
        :param product_description:
        :param product_name:
        :return: product_object
        """
        return cls(product_name, product_description, product_price, product_quantity)

    @staticmethod
    def get_product_name(src_file):
        """
        получаем наименование продукта для класса Products.
        :param prod_list:
        :return:product_name
        """
        product_name = src_file['name']
        return product_name

    @staticmethod
    def get_product_description(src_file):
        """
        получаем описание продукта.
        :param prod_list:
        :return:products_description
        """
        product_description = src_file['description']
        return product_description

    @staticmethod
    def get_product_price(src_file):
        """
        получаем цену продукта.
        :param prod_list:
        :return:product_price
        """
        __product_price = src_file['price']
        return __product_price

    @staticmethod
    def get_product_quantity(src_file):
        """
        получаем количество на складе.
        :param prod_list:
        :return:product_quantity
        """
        product_quantity = src_file['quantity']
        return product_quantity

    # @classmethod
    # def verification(cls, a, new_product_object2):
    #     for i, product in enumerate(a):
    #         print(i, product)
    #         if product['name'] == product_name:
    #             print("Такой есть")
    #             cls.product_quantity += product['quantity']
    #             print(cls.product_quantity)
    #         else:
    #             print("все ок")
    #
    #         #     src_file[i]["products"].append(new_product_object)
    #         #     return src_file
    #         # print(f"Товар не относится к категории {category_name}!")
    #         # return src_file

    # @property
    # def test2(self):
    #     return [product for product in self.__products_list_one_category if product['name'] == self.category_name]
    #
    # @test2.setter
    # def get_prod_in_category(self, category_name):
    #
    #     if category_name == self.category_name:
    #         for product in self.__products_list_one_category:
    #             print(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
    #     else:
    #         print(f'Категория "{category_name}" не найдена в списке категорий.')
