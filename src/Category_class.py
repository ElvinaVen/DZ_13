class Category:
    category_name: str
    category_description: str
    category_products: list
    product_count: int

    category_count = None
    product_count = None

    def __init__(self, category_name, category_description, category_products):
        self.category_name = category_name
        self.category_description = category_description
        self.category_products = category_products

    def __repr__(self):
        return f"Имя категории - {self.category_name}; Описание категории - {self.category_description}; Список продуктов - {self.category_products}\n"
