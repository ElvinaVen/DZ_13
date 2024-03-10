from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

src_file = load_src_file()
# print(f"1) src_file: {src_file}")

print("\n---Задание 1---")
name = "Фрукты"
products_list_one_category2 = Category.get_category_products2(name, src_file)
print(f"3) Список товаров до добавления нового товара: {products_list_one_category2}")
print(f"4) Длина списка товаров до добавления нового: {len(products_list_one_category2)}")
new_product_object = Product.create_new_product_object(product_name='Киви', product_description="Кислый", product_price=90.0, product_quantity=9)
products_list_one_category2 = Category.add_product_in_category2(name, new_product_object, src_file, products_list_one_category2)
print(f"8) Список товаров после добавления нового товара: {products_list_one_category2}")
print(f"9) Длина списка товаров после добавления нового: {len(products_list_one_category2)}")

print("\n---Задание 2---")
name2 = "Фрукты"
print(f"В категории {name2}:")
prod_list = products_list_one_category2
new_category_object = Category.create_new_category_object(name2, category_description='', products_list_one_category=prod_list)
new_category_object.get_prod_in_category = name2

print("\n---Задание 4---")
pr1 = Product(product_name="Киви", product_description="Кислый", product_price=90.0, product_quantity=9)
print(pr1)  # Получение цены
pr1.price = 120  # Установка новой цены
print(pr1.price)  # Получение обновленной цены
print(pr1)
