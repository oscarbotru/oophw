from src.category import Category
from src.product import Product
from src.utils import read_json

if __name__ == '__main__':
    data = read_json('data/products.json')
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product.new_product(product))  # добавленный метод
        category['products'] = products
        categories.append(Category(**category))

    assert categories[0].products == """Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
"""

    product_item = Product('Test', 'Test', 1000, 10)

    product_item.price = 800
    assert product_item.price == 1000

    product_item.price = 1800
    assert product_item.price == 1800
