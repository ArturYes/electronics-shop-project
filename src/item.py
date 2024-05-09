import csv

from config import ROOT_DIR


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError("Складывать можно только экземпляры класса")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10] if len(value) > 10 else value

    @classmethod
    def instantiate_from_csv(cls, patch,):
        cls.all.clear()
        with open(f'{ROOT_DIR + "/" + patch}', 'r', encoding='cp1251') as file:
            csv_data = csv.DictReader(file)
            for line in csv_data:
                name = line['name']
                price = float(line['price'])
                quantity = int(line['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
