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
    def create_product_object(cls, one_category_list):
        """
        Создаем экземпляры класса Product
        :param one_product_dict
        :return: product_object
        """
        # for i in range(len(one_category_list)):

        product_name = cls.get_product_name(one_category_list)
        product_description = cls.get_product_description(one_category_list)
        product_price = cls.get_product_price(one_category_list)
        product_quantity = cls.get_quantity(one_category_list)
        # print(i, product)
        # print(cls(product_name, product_description, product_price, product_quantity))
        return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def create_product_object3(cls, product_name, product_description, product_price, product_quantity):
        """
        Создаем экземпляры класса Product
        :param one_product_dict
        :return: product_object
        """
        # for i in range(len(one_category_list)):

        # product_name = kwargs['product_name']
        # product_description = kwargs['product_description']
        # product_price = kwargs['product_price']
        # product_quantity = kwargs['product_quantity']
        # print(i, product)
        # print(cls(product_name, product_description, product_price, product_quantity))
        return cls(product_name, product_description, product_price, product_quantity)

    @staticmethod
    def get_product_name(prod_list):
        """
        получаем наименование продукта для класса Products.
        :param products_list:
        :return:product_name
        """

        product_name = prod_list['name']
        return product_name

    @staticmethod
    def get_product_description(prod_list):
        """
        получаем описание продукта.
        :param src_file:
        :return:products_description
        """
        product_description = prod_list['description']
        return product_description

    @staticmethod
    def get_product_price(prod_list):
        """
        получаем цену продукта.
        :param products_list:
        :return:product_price
        """
        __product_price = prod_list['price']
        return __product_price

    @staticmethod
    def get_quantity(prod_list):
        """
        получаем количество на складе.
        :param products_list:
        :return:product_quantity
        """
        product_quantity = prod_list['quantity']
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




