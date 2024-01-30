from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass


class PrintMixin:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"


class Product(BaseProduct, PrintMixin):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')


    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n'

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def price(self) -> float:
        return self.price

    @price.setter
    def price(self, new_price: float):
        if new_price < self.price:
            message = input("Подтвердите снижение цены Y - Да, N - Нет ").lower()
            if message == "y":
                self.price = new_price
            return
        self.price = new_price

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class Smartphone(Product, PrintMixin):
    """Класс смартфоны, отдельно существующий продукт"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product, PrintMixin):
    """Класс трава газонная, отдельно существующий продукт"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
