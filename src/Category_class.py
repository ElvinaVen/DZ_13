class Category:
    category_name: str
    category_description: str
    __products_list_one_category: list  # это список товаров данной категории
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов

    def __init__(self, category_name, category_description, products_list_one_category):
        self.category_name = category_name
        self.category_description = category_description
        self.__products_list_one_category = products_list_one_category
        Category.category_count += 1
        Category.product_count += len(self.__products_list_one_category)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.__products_list_one_category}\n"

    @classmethod
    def create_new_category_object(cls, category_name, category_description, products_list_one_category):
        return cls(category_name, category_description, products_list_one_category)

    @property
    def get_prod_in_category(self):
        return [product for product in self.__products_list_one_category if product['name'] == self.category_name]

    @get_prod_in_category.setter
    def get_prod_in_category(self, category_name):

        if category_name == self.category_name:
            for product in self.__products_list_one_category:
                print(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')
        else:
            print(f'Категория "{category_name}" не найдена в списке категорий.')

    @staticmethod
    def get_products(category_name, src_file):
        """
        Получаем список товаров в категории
        :return:category_products
        """
        for category in src_file:
            if category['name'] == category_name:
                return category['products']

    @staticmethod
    def add_product_in_category(category_name, new_product, src_file):
        for i, category in enumerate(src_file):
            if category['name'] == category_name:
                src_file[i]["products"].append(new_product)
            else:
                print(f"Товар не относится к категории {category_name}!")
            return src_file
