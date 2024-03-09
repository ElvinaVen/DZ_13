# from DZ_13_OOP1.src.Product_class import Product
# from DZ_13_OOP1.src.Product_class import Product


class Category:
    category_name: str
    category_description: str
    __products: list  # это список товаров данной категории
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов
    cat_list = []
    prod_list = []

    def __init__(self, category_name, category_description, products):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.__products}\n"

    @classmethod
    def create_category_object(cls, category_list):
        """
        Создаем экземпляры класса Category
        :param category_list
        :return: category_object
        """
        category_name = cls.get_category_name(category_list)
        category_description = cls.get_category_description(category_list)
        category_products = cls.get_category(category_list)
        # print(category_object)
        return cls(category_name, category_description, category_products)

    @classmethod
    def add_category_object(cls, category_object):
        """
        Создаем список всех категорий
        :param category_object:
        :return: cat_list
        """

        cls.cat_list.append(category_object)

    @classmethod
    def get_category_list(cls):
        return cls.cat_list

    @staticmethod
    def set_product(product_list):
        """
        метод для добавления товаров в категорию (в список). Метод должен добавлять в список экземпляр класса Product,
        соответственно список будет состоять из экземлпяров класса Product.
        :param product_obj:принимоет объект класса продукт
        :return:
        """

        __products = product_list
        # print(__products)
        return __products

    @property
    def products(self):
        category_products_string = []
        for product in self.__products:
            category_products_string.append(
                f'{product.product_name}, {product.product_price} руб. Остаток: {product.product_quantity} шт.')
        return 'n'.join(category_products_string)
        # category_products_string = []
        # for product in self.__products:
        #     category_products_string.append(f'{product.product_name}, {product.products_price} руб. Остаток: {product.quantity} шт.')
        #     print(category_products_string)
        # return f'{product.product_name}, {product.products_price} руб. Остаток: {product.quantity} шт.'

    @staticmethod
    def get_category_name(category_list):
        """
        получаем наименование категории
        :return:category_name
        """
        category_name = category_list['name']
        # print(category_name)
        return category_name

    @staticmethod
    def get_category_description(category_list):
        """
        получаем описание категории
        :return:category_description
        """
        category_description = category_list['description']
        # print(category_description)
        return category_description

    @staticmethod
    def get_category(category_list):
        """
        Получаем список товаров в категории
        :return:category_products
        """
        category_products = category_list['products']
        # print(category_products)
        return category_products

# category_object = Category.create_category_object(category_list)
# Category.add_category_object(category_object)
# product_object = Category.create_category_object('Iphone 5', "128GB, Gray space", 10000.0, 3)
# # category_products_string = get_category_products()
# print(product_object.get_category_products)
