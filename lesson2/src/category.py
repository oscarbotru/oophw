class Category:
    """
    Класс для категорий товара
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products

    @property
    def products(self) -> str:
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result
