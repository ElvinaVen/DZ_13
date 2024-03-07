from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import new_product_object, Product
from DZ_13_OOP1.src.utils import load_src_file, create_category_object, create_cat_list, \
    create_products_list

src_file = load_src_file()
cat_list = []
prod_list = []


for i in range(len(src_file)):
    category_list = src_file[i]
    category_object = create_category_object(category_list)
    for j in range(len(src_file[i]['products'])):
        products_list = src_file[i]['products'][j]
        print(products_list)
        # product_object = Product.create_product_object(products_list)
        Product.create_product_object(products_list)

        # product_object = product_object.create_product_object(products_list)
        # Category.create_product()
        # print(product_object)
        Category.add_product_object(product_object)
        prod_list = create_products_list(product_object, prod_list)
    cat_list = create_cat_list(category_object, cat_list)


print(f"Список категорий: {cat_list}")
print(f"Количество категорий: {len(cat_list)}\n")
print(f"Список продуктов: {prod_list}")
print(f"Количество продуктов: {len(prod_list)}")

# cat_list = create_category_list(category_object)
# print(product_object)
# create_category_list(category_object)
# create_category_list(src_file)
# emp1 = Category_class.Category('telek', 'jkhghf', [])
# print(emp1.category_description)

# emp2 = Category_class.Category(category_name, category_description, category_products)
# print(category_object.category_count)
# print(category_object.product_count)



# category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [])
#
# category.add_product(new_product_object)
# print(category)
# print(category.get_category_products)