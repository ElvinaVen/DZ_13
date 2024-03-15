from DZ_13_OOP1.src.Product_class import Product


class Category:
    category_name: str
    category_description: str
    __products: list  # это список товаров данной категории
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов
    products_by_category = {}

    def __init__(self, category_name, category_description, products):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __repr__(self):
        return f"Экз-р категории - {self.category_name}; {self.category_description};  {self.__products}\n"

    # @classmethod
    # def create_new_category_object(cls, category_name, category_description, products_list_one_category):
    #     return cls(category_name, category_description, products_list_one_category)

    # def get_prod_from(self, products_by_category):
    #     result = []
    #     for category in products_by_category:
    #         for prod in category:
    #             result.append(f'{prod["name"]}, {prod["price"]} руб. Остаток: {prod["quantity"]} шт.')
    #             print(prod)
    #             # result.append(f'{prod["name"]}, {prod["price"]} руб. Остаток: {prod["quantity"]} шт.')
    #         return ""

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.product_name}, {product.price} руб. Остаток: {product.product_quantity} шт.\n'
        return result

    # @products.setter
    # def products(self, item):
    #
    #     # if category_name == self.category_name:
    #     #     for product in self.__products_list_one_category:
    #     #         print(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
    #     # else:
    #     #     print(f'Категория "{category_name}" не найдена в списке категорий.')
    #     self.products_list.append(item)

    # @staticmethod
    # def get_products_list(src_file):
    #     """
    #     Получаем список товаров в категории
    #     :return:category_products
    #     """
    #     for category in src_file:
    #         # if category['name'] == category_name:
    #             # print(category['products'])
    #         return category['products']

    # @staticmethod
    # def add_product_in_category(category_name, new_product, src_file):
    #     for i, category in enumerate(src_file):
    #         if category['name'] == category_name:
    #             src_file[i]["products"].append(new_product)
    #             return src_file
    #         print(f"Товар не относится к категории {category_name}!")
    #         return src_file
    # @staticmethod
    # def add_product_in_category2(prod_obj, products_by_category):
    #     # products_by_category = {}
    #     # category_name = category_object.category_name
    #     if prod_obj.category_name in products_by_category:
    #         print(prod_obj.category_name)
    #         products_by_category[prod_obj.category_name].append(prod_obj)
    #         print(products_by_category)
    #     else:
    #         products_by_category[prod_obj.category_name] = [prod_obj]
    #         products_list = products_by_category
    #     return products_list

    # def get(self):
    #     return self.products_list

    # @staticmethod
    # def test(products_by_category):
    #     for category, products_list in products_by_category.items():
    #         print(f"Категория: {category}")
    #         for product in products_list:
    #             print(product)
    #         print()

    @classmethod
    def create_category_object(cls, src_file):
        """
        создаем экз.категории с пустым списком товаров
        :param src_file
        :return: category_object
        """
        category_name = cls.get_category_name(src_file)
        category_description = cls.get_category_description(src_file)
        __products = []
        return cls(category_name, category_description, __products)

    @staticmethod
    def get_category_name(one_category_list):
        """
        получаем наименование категории
        :return:category_name
        """
        category_name = one_category_list['name']
        return category_name

    @staticmethod
    def get_category_description(one_category_list):
        """
        получаем описание категории
        :return:category_description
        """
        category_description = one_category_list['description']
        return category_description

    # @staticmethod
    # def get_category_products(one_category_list):
    #     """
    #     получаем наименование категории
    #     :return:category_name
    #     """
    #     category_products = one_category_list['products']
    #     return category_products

    # @staticmethod
    # def add_new(prod_obj):
    #     __products_list_one_category = []
    #     __products_list_one_category.append(prod_obj)
    #     print(__products_list_one_category)
    #     return __products_list_one_category

    # @staticmethod
    # def get_product_list(self, product_object):
    #     self.__products.append(product_object)
    #     return self.__products

    # def set_product_list(self, product_object):
    #     self.__products.append(product_object)
    #     return self.__products

    @staticmethod
    def adds(new_product_object, total_list, category_name):
        for i, category_info in enumerate(total_list):
            if total_list[i].category_name == category_name:
                total_list[i].__products.append(new_product_object)
        # print(total_list)
        return total_list


    # @staticmethod
    def add_product(self, products1):
        self.__products = products1
        return self.__products

    @staticmethod
    def create_category_products_list(src_file):
        """
        Заполняем список продуктов по категории
        :param src_file:
        :return:
        """
        products_by_category = []
        for j in range(len(src_file['products'])):
            product_object = Product.get_product_object(src_file['products'][j])
            products_by_category.append(product_object)
        return products_by_category


        # print(products_by_category)
        # new_prod_list = products_by_category[category_name]
        # print(new_prod_list)
        # else:
        #     self.products_by_category[category_name] = [prod_obj]

        # new_prod_list = products_by_category[prod_obj.category_name]
        # products_by_category = {}
        # category_name = category_object.category_name
        # if prod_obj.category_name in products_by_category:
        #     print(prod_obj.category_name)
        #     products_by_category[prod_obj.category_name].append(prod_obj)
        #     print(products_by_category)
        # else:
        #     products_by_category[prod_obj.category_name] = [prod_obj]
        #     products_list = products_by_category
        # return products_list
