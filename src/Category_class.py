class Category:
    category_name: str
    category_description: str
    category_products: list
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов

    def __init__(self, category_name, category_description, category_products):
        self.category_name = category_name
        self.category_description = category_description
        self.category_products = category_products
        Category.category_count += 1
        Category.product_count += len(self.category_products)

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.category_products}\n"
