class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < self.__price:
            message = input("Подтвердите снижение цены Y - Да, N - Нет ").lower()
            if message == "y":
                self.__price = new_price
            return
        self.__price = new_price

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity
