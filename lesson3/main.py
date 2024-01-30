from src.product import Product
from src.utils import read_json


if __name__ == '__main__':
    data = read_json('data/products.json')
    products = []
    for category in data:
        for product in category['products']:
            products.append(Product(**product))

    print(products)
