import json


def load_src_file():
    """
    Ф-ия загрузки списка из json.
    :return: src_file - весь список товаров по категориям
    """
    with open('file.json', 'r', encoding='utf-8') as file:
        src_file = json.load(file)
    return src_file


# def get_category_name(category_list):
#     """
#     получаем наименование категории
#     :return:category_name
#     """
#     category_name = category_list['name']
#     # print(category_name)
#     return category_name
#
#
# def get_category_description(category_list):
#     """
#     получаем описание категории
#     :return:category_description
#     """
#     category_description = category_list['description']
#     # print(category_description)
#     return category_description
#
#
# def get_category_products(category_list):
#     """
#     Получаем список товаров в категории
#     :return:category_products
#     """
#     category_products = category_list['products']
#     # print(category_products)
#     return category_products


# def get_product_name(products_list):
#     """
#     получаем наименование продукта для класса Products.
#     :param products_list:
#     :return:product_name
#     """
#     product_name = products_list['name']
#     # print(product_name)
#     return product_name


# def get_product_description(products_list):
#     """
#     получаем описание продукта.
#     :param products_list:
#     :return:products_description
#     """
#     products_description = products_list['description']
#     # print(products_description)
#     return products_description
#
#
# def get_products_price(products_list):
#     """
#     получаем цену продукта.
#     :param products_list:
#     :return:product_price
#     """
#     product_price = products_list['price']
#     # print(product_price)
#     return product_price


# def get_quantity(products_list):
#     """
#     получаем количество на складе.
#     :param products_list:
#     :return:product_quantity
#     """
#     product_quantity = products_list['quantity']
#     # print(product_quantity)
#     return product_quantity


# def create_category_object(category_list):
#     """
#     Создаем экземпляры класса Category
#     :param category_list
#     :return: category_object
#     """
#     category_name = get_category_name(category_list)
#     category_description = get_category_description(category_list)
#     category_products = get_category_products(category_list)
#     category_object = Category_class.Category(category_name, category_description, category_products)
#     # print(category_object)
#     return category_object


# def create_product_object(products_list):
#     """
#     Создаем экземпляры класса Product
#     :param products_list
#     :return: product_object
#
#     """
#     product_name = get_product_name(products_list)
#     product_description = get_product_description(products_list)
#     product_price = get_products_price(products_list)
#     product_quantity = get_quantity(products_list)
#     product_object = Product(product_name, product_description, product_price, product_quantity)
#     return product_object


# def create_cat_list(category_object, cat_list):
#     """
#     Создаем список всех категорий
#     :param cat_list:
#     :param category_object:
#     :return: cat_list
#     """
#     cat_list.append(category_object)
#     # print(cat_list)
#     return cat_list


# def create_products_list(product_object, prod_list):
#     """
#
#     :param product_object, prod_list:
#     :return: products_list
#     """
#     prod_list.append(product_object)
#     # print(prod_list)
#     return prod_list
