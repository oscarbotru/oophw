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

    def __str__(self):
        total_products_count = sum([p.price for p in self.__products])
        return f'{self.name}, количество продуктов: {total_products_count} шт.'

    @property
    def products(self) -> str:
        result = ''
        for product in self.__products:
            result += f'{product}\n'

        return result
