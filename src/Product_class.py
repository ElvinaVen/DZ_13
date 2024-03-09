from DZ_13_OOP1.src.Category_class import Category


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

    @classmethod
    def add_product_object_in_prod_list(cls, product_object):
        """
        Создаем список всех товаров

        :param product_object:
        :return: prod_list
        """

        cls.prod_list.append(product_object)
        return cls.prod_list  # список всех категорий

    # @classmethod
    # def get_product_list(cls):
    #     return cls.prod_list

    # @classmethod
    # def add_in_category(cls, prod):
    #     return Category.set_product(prod)


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
