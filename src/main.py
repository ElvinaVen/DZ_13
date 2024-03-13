from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

# Овощи Фрукты - это для подставления в name1 и name2

src_file = load_src_file()
# print(src_file)

print("\n---Задание 1---")
def full_total_category_list():
    total_list = []
    for i in range(len(src_file)):
        category_object = Category.create_category_object(src_file[i])
        # create_product_object3()
        # print(f"Экземпляр категории до: {category_object}\n")
        products1 = create_category_products_list(src_file[i])  # [Экз-р продукта - Бананы, Желтые, 120.0, 12, Экз-р продукта - Яблоки, Красные, 80.0, 8, Экз-р продукта - Груши, Зеленые, 140.0, 14]
        products = category_object.add_product(products1)
        print(f"Список продуктов экз-ра категории: {products}\n")
        print(f"Экземпляр категории после: {category_object}\n")
        total_list.append(category_object)
        print(f"Экземпляр категории после: {total_list}\n")
        print("-----------------------------------------------------------------")

    return total_list

def create_category_products_list(src_file):
    # name1 = "Фрукты"
    products1 = []
    for j in range(len(src_file['products'])):
        prod_list = src_file['products'][j]
        # products.join(Product.create_product_object(prod_list))
        products1.append(Product.create_product_object(prod_list))
    print(f"продактс это список: {products1}\n")
    return products1

print("-----------------------------------------------------------------")
total_list = full_total_category_list()
print(f"Общий список всех категорий с продуктами:{total_list}")
category_name = "Фрукты"
#
new_product_object = Product.create_product_object3('Киви', "Кислый", 90.0, 9)
print(new_product_object)
Category.adds(new_product_object, total_list, category_name)
print(total_list)
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

