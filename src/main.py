from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

src_file = load_src_file()
# cat_list = []
# prod_list = []

for i in range(len(src_file)):
    one_category_list = src_file[i]
    # print(src_file[i])
    # print(one_category_list)
    category_object = Category.create_category_object(one_category_list)  # создаем экз-ры класса Категории
    # print(category_object)
    cat_list = Category.add_category_object_in_cat_list(category_object)  # добавляем экз-ры в список cat_list
    # print(cat_list)
    # print(category_object.products)
    # print(category_object.products_list_one_category)
# print(f"Список категорий: {cat_list}")
# print(f"Количество категорий: {len(cat_list)}\n")

for i in range(len(src_file)):
    for j in range(len(src_file[i]['products'])):
        one_product_dict = src_file[i]['products'][j]
        # print(one_product_dict)
        product_object = Product.create_product_object(one_product_dict)  # создаем экз-ры класса Продукты
        prod_list = Product.add_product_object_in_prod_list(product_object)  # добавляем экз-ры в список prod_list

    # print(f"Список продуктов одной категории: {prod_list}")
    # print(f"Количество продуктов: {Category.product_count}\n")

new_product_object = Product.create_new_product_object('Iphone 5', "128GB, Gray space", 10000.0, 3)

# new_product_object = Product.create_new_product_object('Iphone 5', "128GB, Gray space", 10000.0, 3)

print(new_product_object)
new_category_object = Category.create_new_category_object("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ])
#
# new_category_object.add_to_private_list(new_product_object)
# private_list = new_category_object.get_private_list()
# print(f"Список товаров после добавления нового: {private_list}")
# print(len(private_list))

# for item in prod_list:
# print(category_object.products_list_one_category)
    # print(item.products_list_one_category)
    # print(f"{item["name"]}, {item["price"]} руб. Остаток: {item["quantity"]} шт.")



# print(category_object.products)

# print(Category.get_category_list())
# print(Category.get_category_name(src_file))
# print(category_object.category_name)
# print(category_object.category_description)
# print(category_object.products_list_one_category) #  НЕЛЬЗЯ, т.к. он приватный

print(new_category_object.get_prod_in_category("Смартфоны"))

