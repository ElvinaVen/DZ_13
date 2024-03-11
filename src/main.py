from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

# Овощи Фрукты - это для подставления в name1 и name2

src_file = load_src_file()
print("\n---Задание 1---")
name1 = "Фрукты"

print(f"3) Список товаров до добавления нового товара: {Category.get_products(name1, src_file)}")
print(f"4) Длина списка товаров до добавления нового товара: {len(Category.get_products(name1, src_file))}")
new_product_object = Product.create_new_product_object(product_name='Киви', product_description="Кислый", product_price=90.0, product_quantity=9)
src_file = Category.add_product_in_category(name1, new_product_object, src_file)
print(f"8) Список товаров после добавления нового товара: {Category.get_products(name1, src_file)}")
print(f"9) Длина списка товаров после добавления нового: {len(Category.get_products(name1, src_file))}")

print("\n---Задание 2---")
name2 = "Овощи"
print(f"В категории {name2}:")
prod_list = Category.get_products(name2, src_file)
new_category_object = Category.create_new_category_object(name2, category_description='', products_list_one_category=prod_list)
new_category_object.get_prod_in_category = name2

print("\n---Задание 4---")
pr1 = Product(product_name="Киви", product_description="Кислый", product_price=90.0, product_quantity=9)
print(pr1)  # Получение цены
pr1.price = 120.0  # Установка новой цены
print(pr1.price)  # Получение обновленной цены
print(pr1)
