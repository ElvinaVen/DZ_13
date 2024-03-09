# from DZ_13_OOP1.src.Product_class import Product
# from DZ_13_OOP1.src.Product_class import Product


class Category:
    category_name: str
    category_description: str
    __products_list_one_category: list  # это список товаров данной категории
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов
    cat_list = []
    prod_list = []

    def __init__(self, category_name, category_description, products_list_one_category):
        self.category_name = category_name
        self.category_description = category_description
        self.__products_list_one_category = products_list_one_category
        Category.category_count += 1
        Category.product_count += len(self.__products_list_one_category)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.__products_list_one_category}\n"

    @classmethod
    def create_category_object(cls, one_category_list):
        """
        Создаем экземпляры класса Category
        :param one_category_list
        :return: category_object
        """
        category_name = cls.get_category_name(one_category_list)
        category_description = cls.get_category_description(one_category_list)
        products_list_one_category = cls.get_category_products(one_category_list)
        # print(category_object)
        return cls(category_name, category_description, products_list_one_category)

    @classmethod
    def add_category_object_in_cat_list(cls, category_object):
        """
        Добавляем в список категорий/ объекты категорий
        :param category_object:
        :return: cat_list список всех категорий
        """
        cls.cat_list.append(category_object)
        return cls.cat_list  # список всех категорий

    # @classmethod
    # def get_category_list(cls):
    #     return cls.cat_list   # список всех категорий

    # def set_product(self, product_object):
    #     """
    #     метод для добавления товаров в категорию (в список). Метод должен добавлять в список экземпляр класса Product,
    #     соответственно список будет состоять из экземлпяров класса Product.
    #     :param product_object: принимоет объект класса продукт
    #     :return:
    #     """
    #
    #     self.__products_list_one_category.append(product_object)
    #     # print(a)
    #     # return cls.__products_list_one_category

    def add_to_private_list(self, product_object):
        '''
         метод для добавления товара в категорию
        :param product_object:принимоет объект класса продукт
        '''
        self.__products_list_one_category.append(product_object)

    def get_private_list(self):
        """
        возвращает текущий список товаров после добавления
        :return:
        """
        # print(self.__products_list_one_category)
        return self.__products_list_one_category

    @classmethod
    def create_new_category_object(cls, category_name, category_description, products_list_one_category):
        return cls(category_name, category_description, products_list_one_category)

    # def add_product_to_category(self, product_object):
    #     """
    #
    #     :param product_object:
    #     :return:
    #     """
    #     self.set_product(product_object)

    # def get_products_list(self):
    #     return self.product

    # cls.prod_list.append(product_object)
    # return cls.prod_list  # список всех категорий

    # @property
    # def products_list_one_category(self, category_name):
    #     category_products_string = ""
    #     for product in self.__products_list_one_category:
    #         category_products_string += f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.'
    #     return category_products_string

    def get_prod_in_category(self, category_name):
        if category_name == self.category_name:
            print(f'Категория "{category_name}" найдена в списке категорий.')
            for i in range(len(self.__products_list_one_category)):
                print(f'{self.__products_list_one_category[i]['name']}, {self.__products_list_one_category[i]["price"]} руб. Остаток: {self.__products_list_one_category[i]["quantity"]} шт.')
        else:
            return f'Категория "{category_name}" не найдена в списке категорий.'


        # category_products_string = []
        # for product in self.__products:
        #     category_products_string.append(f'{product.product_name}, {product.products_price} руб. Остаток: {product.quantity} шт.')
        #     print(category_products_string)
        # return f'{product.product_name}, {product.products_price} руб. Остаток: {product.quantity} шт.'

    @staticmethod
    def get_category_name(one_category_list):
        """
        получаем наименование категории
        :return:category_name
        """
        category_name = one_category_list['name']
        # print(category_name)
        return category_name

    @staticmethod
    def get_category_description(one_category_list):
        """
        получаем описание категории
        :return:category_description
        """
        category_description = one_category_list['description']
        # print(category_description)
        return category_description

    @staticmethod
    def get_category_products(one_category_list):
        """
        Получаем список товаров в категории
        :return:category_products
        """
        products_list_one_category = one_category_list['products']
        # print(products_list_one_category)
        return products_list_one_category

    def get_telek(self, category_name):
        pass

# category_object = Category.create_category_object(category_list)
# Category.add_category_object(category_object)
# product_object = Category.create_category_object('Iphone 5', "128GB, Gray space", 10000.0, 3)
# # category_products_string = get_category_products()
# print(product_object.get_category_products)
# category_object = '<DZ_13_OOP1.src.Category_class.Category object at 0x00000267B47867B0>'
# print(category_object.category_description)
