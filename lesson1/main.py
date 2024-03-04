from src.category import Category
from src.product import Product
from src.utils import read_json


if __name__ == '__main__':
    data = read_json('data/products.json')
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

