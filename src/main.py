from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product

from DZ_13_OOP1.src.utils import load_src_file

src_file = load_src_file()
print(f"1) src_file: {src_file}")
cat_list = []

for i in range(len(src_file)):
    one_category_dict = src_file[i]
    print(f"2) one_category_dict: {one_category_dict}")
    category_object = Category.create_category_object(one_category_dict)  # создаем экз-ры класса Категории
    cat_list = Category.add_category_object_in_cat_list(cat_list, category_object)  # добавляем экз-ры в список cat_list
    prod_list = []
    for j in range(len(src_file[i]['products'])):
        one_product_dict = src_file[i]['products'][j]
        print(f"2) one_product_dict: {one_product_dict}")
        product_object = Product.create_product_object(one_product_dict)  # создаем экз-ры класса Продукты
        prod_list = Product.add_product_object_in_prod_list(prod_list, product_object)  # добавляем экз-ры в список prod_list
    print(f"3) prod_list Список товаров одной категории: {prod_list}")
    print(f"4) Количество товаров одной категории: {len(prod_list)}\n")

print(f"5) cat_list Список категорий: {cat_list}")
print(f"6) Количество категорий: {len(cat_list)}\n")

new_product_object = Product.create_new_product_object(product_name='Киви', product_description="Кислый", product_price=90.0, product_quantity=9)
category_object = Category("Фрукты","Сладкие, сочные",[{"name": "Бананы","description": "Желтые","price": 120.0,"quantity": 12 },{"name": "Яблоки","description": "Красные","price": 80.0, "quantity": 8},{"name": "Груши","description": "Зеленые","price": 140.0,"quantity": 14}])
# category_object.add_to_private_list(new_product_object, 'Фрукты', prod_list)

private_list = category_object.get_private_list(prod_list)
print(f"8) private_list Список товаров после добавления нового: {private_list}")
print(f"9) Длина списка товаров после добавления нового: {len(private_list)}")

