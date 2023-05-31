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
        self.number_of_sim = number_of_sim

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

    @property
    def number_of_sim(self) -> int:
        '''
        Возвращает кол-во поддерживаемых
        сим-карт
        '''
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        '''
        Устснавливает значение поддерживаемых
        сим-карт, проверяя является ли значение
        положительным. В конечном итоге возвращает
        целое от числа или ошибку, если значение окажется
        отрицательным
        '''
        if isinstance(value, int) and value > 0:
            self._number_of_sim = int(value)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
