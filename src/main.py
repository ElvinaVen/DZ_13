from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

# Овощи Фрукты - это для подставления в name1 и name2

src_file = load_src_file()
print(src_file)

print("\n---Задание 1---")
products_by_category = {}
name1 = "Фрукты"
for i in range(len(src_file)):
    one_category_list = src_file[i]
    category_object = Category.create_category_object(one_category_list)
    # print(f"---{one_category_list}")
    for j in range(len(one_category_list['products'])):
        prod_list = one_category_list['products'][j]
        prod_obj = Product.create_product_object(prod_list)
        # print(type(prod_obj))
        # print(prod_obj)
        # Добавляем продукт в список продуктов категории в словаре
        category_name = category_object.category_name
        if category_name in products_by_category:
            products_by_category[category_name].append(prod_obj)
            # new_prod_list = products_by_category[category_name]
            # print(new_prod_list)
        else:
            products_by_category[category_name] = [prod_obj]
        # print("+++")
        new_prod_list = products_by_category[category_name]
        # print(new_prod_list)
print("---")

    # print(prod_list)
    # Выводим результат
print(f"Общий список продуктов по категориям {products_by_category}")
for category, products_list in products_by_category.items():
    print(f"Категория: {category}")
    for product in products_list:
        print(product)
    print()
# print(category_object.category_name)
# Category.add_product_in_category2(prod_obj, category_object)
# print(Category.get)

    # Category.get_product_list(prod_obj)
    # print(Category.get_product_list(prod_obj))
    # Category.get_product_list(prod_obj)
    # print(prod_list)
    # print(prod_obj)

# Category.add(prod_obj)

# print(f"3) Список товаров до добавления нового товара: {Category.add_new(prod_obj)}")

# # print(f"4) Длина списка товаров до добавления нового товара: {len(Category.get_products(name1, src_file))}")
# new_product_object = Product.create_new_product_object(product_name='Киви', product_description="Кислый", product_price=90.0, product_quantity=9)
new_product_object = Product.create_product_object3('Киви', "Кислый", 90.0, 9)
# print(type(new_product_object))
print(new_product_object)
category_name = "Фрукты"
# category_name = new_product_object.category_name
if category_name in products_by_category:
    products_by_category[category_name].append(new_product_object)
    # new_prod_list = products_by_category[category_name]
    # print(new_prod_list)
else:
    products_by_category[category_name] = [new_product_object]
print(f"Общий список продуктов по категориям {products_by_category}")
# new_product_object = Product.create_product_object('Киви', "Кислый", 90.0, 9)
# Category.add_product_in_category2(new_product_object, products_by_category)

# print(f"8) Список товаров после добавления нового товара: {Category.get_products(name1, src_file)}")
# print(f"9) Длина списка товаров после добавления нового: {len(Category.get_products(name1, src_file))}")
# print(src_file[0].product_name)

# print("\n---Задание 2---")
# name2 = "Овощи"
# print(f"В категории {name2}:")
# prod_list = Category.get_products(name2, src_file)
# new_category_object = Category.create_new_category_object(name2, category_description='', products_list_one_category=prod_list)
# new_category_object.get_prod_in_category = name2

# print("\n---Задание 4---")
# pr1 = Product(product_name="Киви", product_description="Кислый", product_price=90.0, product_quantity=9)
# print(pr1)  # Получение цены
# pr1.price = 120.0  # Установка новой цены
# print(pr1.price)  # Получение обновленной цены
# print(pr1)
# print(f"Общий список продуктов по категориям {products_by_category}")

