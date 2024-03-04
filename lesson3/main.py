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

    product_item = Product('Test', 'Test', 1000, 10)

    assert str(product_item) == 'Test, 1000 руб. Остаток: 10 шт.'

    product_item_2 = Product('Test2', 'Test2', 500, 20)

    assert product_item + product_item_2 == 20000
