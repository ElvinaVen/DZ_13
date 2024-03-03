from DZ_13_OOP1.src.utils import load_src_file, create_category_list, create_products_list

url = 'https://jsonkeeper.com/b/8NUV'

src_file = load_src_file(url)
category_list = create_category_list(src_file)
products_list = create_products_list(src_file)
