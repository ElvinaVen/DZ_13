class Product:
    product_name: str
    product_description: str
    product_price: float
    product_quantity: int  # количество в наличии
    prod_list = []

    def __init__(self, product_name, product_description, product_price, product_quantity):

        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_quantity = product_quantity

    # def __repr__(self):
    #     return (f"Имя продукта - {self.product_name} Описание продукта - {self.product_description} "
    #             f"Стоимость продукта - {self.product_price} Количество - {self.product_quantity}")

    @classmethod
    def create_product_object(cls, products_list):
        """
        Создаем экземпляры класса Product
        :param products_list
        :return: product_object

        """
        product_name = cls.get_product_name(products_list)
        product_description = cls.get_product_description(products_list)
        product_price = cls.get_products_price(products_list)
        product_quantity = cls.get_quantity(products_list)
        # product_object = Product(product_name, product_description, product_price, product_quantity)
        return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def add_product_object(cls, product_object):
        """
        Создаем список всех категорий

        :param product_object:
        :return: cat_list
        """

        cls.prod_list.append(product_object)

    @classmethod
    def get_product_list(cls):
        return cls.prod_list

    # @staticmethod
    # def create_products_list(product_object, prod_list):
    #     """
    #
    #     :param product_object, prod_list:
    #     :return: products_list
    #     """
    #     prod_list.append(product_object)
    #     # print(prod_list)
    #     return prod_list

    @classmethod
    def create_new_product_object(cls, product_name, product_description, product_price, product_quantity):
        """
        создали новый экземпляр класса Product
        :param product_name:
        :param product_description:
        :param product_price:
        :param product_quantity:
        :return: new_product_object
        """
        # new_product_object = cls(product_name, product_description, product_price, product_quantity)
        #
        return cls(product_name, product_description, product_price, product_quantity)

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
        # print(product_name)
        return product_name

    @staticmethod
    def get_product_description(products_list):
        """
        получаем описание продукта.
        :param products_list:
        :return:products_description
        """
        products_description = products_list['description']
        # print(products_description)
        return products_description

    @staticmethod
    def get_products_price(products_list):
        """
        получаем цену продукта.
        :param products_list:
        :return:product_price
        """
        product_price = products_list['price']
        # print(product_price)
        return product_price

    @staticmethod
    def get_quantity(products_list):
        """
        получаем количество на складе.
        :param products_list:
        :return:product_quantity
        """
        product_quantity = products_list['quantity']
        # print(product_quantity)
        return product_quantity

# emp = Product('Iphone 5', "128GB, Gray space", 10000.0, 3)
# print(emp.get_category_products)


# print(new_product_object)
# new_product_object = Product('Iphone 5', "128GB, Gray space", 10000.0, 3)

# print(new_product_object.product_price_func)
# new_product_object.product_price_func = 2000
# print(new_product_object.product_price_func)
