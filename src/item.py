import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV = os.path.abspath('../src/items.csv')

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
        return f'{self.__class__.__name__}' \
               f'{self.name, self.price, self.quantity}'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

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

    @property
    def name(self) -> str:
        """
        Возвращает имя товара
        :return: имя товара
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Устанавливает имя товара, проверяя,
        что имя более 1 символа и не привышает 10
        символов
        """
        if len(value) > 10:
            print("Длина названия товара не "
                  "должна превышать 10 символов")
        elif len(value) == 0:
            print("Длина названия должна иметь "
                  "хотябы 1 символ")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls) -> None:
        '''
        Инициализирует экземпляры класса,
        получая обьекты из csv файла
        '''
        cls.all.clear()
        try:
            with open(cls.CSV, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Файл не найден")

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Переводит строку в число
        :return: число из числа-строки
        """
        data = float(string)
        return int(data)
