from src.category import Category
from src.product import Product, Smartphone, LawnGrass
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
    product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
    product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')
