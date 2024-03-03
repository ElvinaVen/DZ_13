import pytest
from DZ_13_OOP1.src.utils import create_category_object


@pytest.fixture
def src_file():
    return [{'name': 'Смартфоны',
             'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
             'products': [{'name': 'Samsung Galaxy C23 Ultra',
                           'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
                           'quantity': 5},
                          {'name': 'Iphone 15', 'description': '512GB, Gray space',
                           'price': 210000.0, 'quantity': 8}]},
            {'name': 'Телевизоры',
             'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
             'products': [{'name': '55" QLED 4K',
                           'description': 'Фоновая подсветка',
                           'price': 123000.0,
                           'quantity': 7}]}]


def test_initial_value(src_file):
    category_object = create_category_object(src_file[0])
    assert category_object.category_name == 'Смартфоны'
    assert category_object.category_description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category_object.category_products == [{'name': 'Samsung Galaxy C23 Ultra',
                                                  'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
                                                  'quantity': 5},
                                                 {'name': 'Iphone 15', 'description': '512GB, Gray space',
                                                  'price': 210000.0, 'quantity': 8}]
