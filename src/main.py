from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

# Овощи Фрукты - это для подставления в name1 и name2

src_file = load_src_file()

print("\n---Задание 1---")

total_list = []
# def full_total_category_list():

for i in range(len(src_file)):
    category_object = Category.create_category_object(src_file[i])  # создаем экз.категории с пустым списком товаров
    print(f"Экземпляр категории с пустым списком: {category_object}\n")
    products_by_category = Category.create_category_products_list(src_file[i])  # заполняем список товаров
    category_object.add_product(products_by_category)
    # print(f"Список продуктов экз-ра категории: {products}\n")
    print(f"Экземпляр категории с заполненным списком: {category_object}\n")
    total_list.append(category_object)
    print(category_object.products)
    # print(f"Экземпляр категории после: {total_list}\n")
    print(total_list)
    # return total_list

print("-----------------------------------------------------------------")
# total_list = full_total_category_list()
print(f"Общий список всех категорий с продуктами:{total_list}\n")

category_name = "Фрукты"
#
new_product_object = Product.create_new_product_object('Киви', "Кислый", 90.0, 9)
print(f"Новый товар: {new_product_object}\n")
Category.adds(new_product_object, total_list, category_name)
print(f"Общий список всех категорий с новым товаром:{total_list}")

# category_name = "Фрукты"
# Category.adds(new_product_object, Category.products_by_category, category_name)
print("-----------------------------------------------------------------")

# # new_product_object = Product.create_new_product_object(product_name='Киви', product_description="Кислый", product_price=90.0, product_quantity=9)
#
# new_product_object = Product.create_product_object3('Киви', "Кислый", 90.0, 9)
# category_name = "Фрукты"
# Category.adds(new_product_object, Category.products_by_category, category_name)
# # print(f"Общий список продуктов по категориям после {Category.products_by_category}")
# for category, products_list in Category.products_by_category.items():
#     # print(f"Категория: {category}")
#     for product in products_list:
#         print(product)
#     print()

print("\n---Задание 2---")
# category_object.products
# category_object.
# def abcd(total_list):
#     for category_info in total_list:
#         category_name = category_info.category_name
#         product_info = category_info.products
#
#         print(f"Категория: {category_name}")
#
#         for product in range(total_list):
#             product_name = product.product_name
#             product_description = product.product_description
#             product_price = product.product_price
#             product_quantity = product.product_quantity
#
#             # print(
#             #     f"Товар: {product_name}, Описание: {product_description}, Цена: {product_price}, Количество: {product_quantity}")
#         return f"Товар: {product_name}, Описание: {product_description}, Цена: {product_price}, Количество: {product_quantity}"
# #
# c = abcd(total_list)
# print(c)
# name2 = "Овощи"
# print(f"В категории {name2}:")
# for category, products in total_list:
#     print(f"Категория: {category}")
#     for product in products:
#         print(category.products)
#     print()


# def abc():
#     for category, products_list in Category.products_by_category.items():
#         print(f"Категория: {category}")

# print(products_list)
# print(products_list.products())


#
# abc()


# list =
# for product in category_products:
#     for i in products_by_category['Фрукты']:
#         print(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.')


# print("n---Общий список продуктов по категориям---")
# for category_name, products in products_by_category.items():
#     print(f"n---{category_name}---")
#     for product in products:
#
#         print(f'{product.get_prod_in_category}')

# new_category_object2 = Category.create_new_category_object(name2, category_description='', products_list_one_category=prod_list)
# new_category_object2.get_prod_in_category = name2

# print("\n---Задание 4---")
# pr1 = Product(product_name="Киви", product_description="Кислый", product_price=90.0, product_quantity=9)
# print(pr1)  # Получение цены
# pr1.price = 120.0  # Установка новой цены
# print(pr1.price)  # Получение обновленной цены
# print(pr1)
# print(f"Общий список продуктов по категориям {products_by_category}")
