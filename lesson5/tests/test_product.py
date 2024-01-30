import pytest
from src.product import Product


@pytest.fixture
def products_():
    return Product(
        'Продукт',
        'Описание продукта',
        100.00,
        12
    )


def test_product_init(products_):
    assert products_.name == 'Продукт'
    assert products_.description == 'Описание продукта'
    assert products_.price == 100.00
    assert products_.count == 12
