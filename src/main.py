from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

src_file = load_src_file()
cat_list = []
prod_list = []

for i in range(len(src_file)):
    category_list = src_file[i]
    # print(src_file[i])
    # print(category_list)
    category_object = Category.create_category_object(category_list)
    Category.add_category_object(category_object)
    # print(category_object.products)
    # print(f"Объект категорий: {category_object}")
cat_list = Category.get_category_list()
# print(f"Список категорий: {cat_list}")
# print(f"Количество категорий: {len(cat_list)}\n")
# print(category_object.products)
# category_object.get_category_products
# category_products_string = category_object.get_category_products

for i in range(len(src_file)):
    for j in range(len(src_file[i]['products'])):
        products_list = src_file[i]['products'][j]
        # print(products_list)
        product_object = Product.create_product_object(products_list)
        Product.add_product_object(product_object)
        print(
            f'{product_object.product_name}, {product_object.product_price} руб. Остаток: {product_object.product_quantity} шт.')
        # print(product_object)
    prod_list = Product.get_product_list()
    print(f"Список продуктов одной категории: {prod_list}")
    print(f"Количество продуктов: {len(prod_list)}\n")

# new_product_object = Product.create_new_product_object('Iphone 5', "128GB, Gray space", 10000.0, 3)
# print("Создали новый продукт:", new_product_object)
# Product.add_product_object(new_product_object)
# prod_list = Product.get_product_list()

# print(f"Список продуктов после добавления: {prod_list}")
# print(f"Количество продуктов после добавления: {len(prod_list)}\n")


# print(category_object.products)

