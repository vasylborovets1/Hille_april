from items import Item


class Sword(Item):

    def __init__(self, name: str, price: int or float, power_bonus: int or float):
        super().__init__(name, price)
        if power_bonus > 0:
            self.__power_bonus = power_bonus
        else:
            raise ValueError('Power bonus must be above 0')

    @property
    def power_bonus(self):
        return self.__power_bonus

    @power_bonus.setter
    def power_bonus(self, value):
        if value > 0:
            self.__power_bonus = round(value, 2)
        else:
            raise ValueError('Power bonus must be above 0')


if __name__ == '__main__':
    sword = Sword(name='Sword', price=100, power_bonus=10)
    print(sword)
