from DZ_13_OOP1.src.Product_class import new_product_object


# from DZ_13_OOP1.src.main import category_object
# from DZ_13_OOP1.src.utils import load_src_file, create_category_object


class Category:
    category_name: str
    category_description: str
    __products: list  # это список товаров
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов

    def __init__(self, category_name, category_description, products):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.__products}\n"

    def add_product_object(self, product_obj):
        """
        метод для добавления товаров в категорию (в список). Метод должен добавлять в список экземпляр класса Product,
        соответственно список будет состоять из экземлпяров класса Product.
        :param product_obj:принимоет объект класса продукт
        :return:
        """
        self.__products.append(product_obj)
        print(f'Список всех товаров {self.__products}')

    @property
    def get_category_products(self):
        category_products = ''
        for product in self.__products:
            category_products += f'{product.product_name}, {product.product_price} руб. Остаток: {product.product_quantity} шт.'
            # print(category_products)
        return category_products

    # def get_category_name(category_list):
    #     """
    #     получаем наименование категории
    #     :return:category_name
    #     """
    #     category_name = category_list['name']
    #     # print(category_name)
    #     return category_name


# print(new_product_object.get_category_products)
# Category.add_product(new_product_object)
# print(Category.category_description)
# product_object = Product('Iphone 5', "128GB, Gray space", 10000.0, 3)
# src_file = load_src_file()
# for i in range(len(src_file)):
#     category_object = create_category_object(src_file[i])


# category_object.add_product(product_object)
# a = category_object.add_product(new_product_object)
# print(a)

category = Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [])
category.add_product_object(new_product_object)
print(category.get_category_products)
