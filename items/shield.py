from items import Item


class Shield(Item):

    def __init__(self, name: str, price: int or float, defence_bonus: int or float):
        super().__init__(name, price)
        if defence_bonus > 0:
            self.__defence_bonus = defence_bonus
        else:
            raise ValueError('Defence bonus bonus must be above 0')

    @property
    def defence_bonus(self):
        return self.__defence_bonus

    @defence_bonus.setter
    def defence_bonus(self, value):
        if value > 0:
            self.__defence_bonus = round(value, 2)
        else:
            raise ValueError('Defence bonus must be above 0')


if __name__ == '__main__':
    shield = Shield(name='Shield', price=100, defence_bonus=10)
    print(shield)
