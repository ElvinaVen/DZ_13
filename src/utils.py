import requests
import urllib3
from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product

urllib3.disable_warnings()


def load_src_file(url):
    """
    Ф-ия загрузки списка из url
    :param url: 'https://jsonkeeper.com/b/8NUV'
    :return: src_file - весь список товаров по категориям
    """
    response = requests.get(url, verify=False)
    src_file = response.json()
    return src_file


def create_category_object(src_file):
    """
    Создаем экземпляры класса Category
    :param src_file
    :return: category_object
    """
    category_name = src_file['name']
    category_description = src_file['description']
    category_products = src_file['products']
    category_object = Category(category_name, category_description, category_products)
    return category_object


def create_product_object(products_list):
    """
    Создаем экземпляры класса Product
    :param products_list
    :return: product_object

    """
    product_name = products_list['name']
    product_description = products_list['description']
    product_price = products_list['price']
    product_quantity = products_list['quantity']
    product_object = Product(product_name, product_description, product_price, product_quantity)
    return product_object


def create_category_list(src_file):
    """

    :param src_file:
    :return: category_list
    """
    category_list = []

    for i in range(len(src_file)):
        category_object = create_category_object(src_file[i])
        category_list.append(category_object)
    Category.category_count = len(category_list)
    print(f"Список категорий: {category_list}")
    print(f"Количество категорий: {Category.category_count}")
    return category_list


def create_products_list(src_file):
    """

    :param src_file:
    :return: products_list
    """
    products_list = []
    count_product_object = 0

    for i in range(len(src_file)):
        for j in range(len(src_file[i]['products'])):
            product_object = create_product_object(src_file[i]['products'][j])
            count_product_object += 1
            products_list.append(product_object)
    Category.product_count = len(products_list)
    print(f"Список продуктов: {products_list}")
    print(f"Количество уникальных продуктов: {Category.product_count}")
    return products_list
