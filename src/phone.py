from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        '''
        Создание экземпляра класса Phone
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Кол-во поддерживаемых сим-кард
        '''
        super().__init__(name, price, quantity)
        self.__number_of_sim = self.__check_number_of_sim(number_of_sim)

    def __add__(self, other) -> int:
        '''
        Складывает два обьекты, относящиеся к
        классу Phone или Item
        '''
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}' \
               f'{self.name, self.price, self.quantity, self.number_of_sim}'

    def __check_number_of_sim(self, value) -> int:
        '''
        Проверяет кол-во поддерживаемых сим-карт:
        если число больше 0, то возвращает
        целое значение данного числа, иначе
        просто 1
        '''
        if value > 0:
            return int(value)
        return 1

    @property
    def number_of_sim(self) -> int:
        '''
        Возвращает кол-во поддерживаемых
        сим-карт
        '''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        '''
        Устснавливает значение поддерживаемых
        сим-карт, проверяя является ли значение
        положительным. В конечном итоге возвращает
        целое от числа или 1, если значение окажется
        отрицательным
        '''
        if value > 0:
            self.__number_of_sim = value
        else:
            self.__number_of_sim = 1
