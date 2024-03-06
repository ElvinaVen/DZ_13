from DZ_13_OOP1.src.Product_class import Product
# from DZ_13_OOP1.src.main import category_object
# from DZ_13_OOP1.src.utils import load_src_file, create_category_object


class Category:
    category_name: str
    category_description: str
    __products: list
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов

    def __init__(self, category_name, category_description, category_products):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = category_products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.__products}\n"

    def add_product(self, new_product_object):
        # self.__category_products.append(product_object)
        self.__products.append(new_product_object)
        # print(self.__products)
        return self.__products

    @property
    def get_category_products(self):
        result = ''
        for product in self.__products:
            result += f'{product.product_name}, {product.product_price} руб. Остаток: {product.product_quantity} шт.'
            print(result)
        return result

new_product_object = Product.create_product('Iphone 5', "128GB, Gray space", 10000.0, 3)
# product_object = Product('Iphone 5', "128GB, Gray space", 10000.0, 3)
# src_file = load_src_file()
# for i in range(len(src_file)):
#     category_object = create_category_object(src_file[i])


# category_object.add_product(product_object)
# a = category_object.add_product(new_product_object)
# print(a)
