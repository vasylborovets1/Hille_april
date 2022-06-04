class Item:

    def __init__(self, name: str, price: int or float):
        self.__name = name
        if price > 0:
            self.__price = price
        else:
            raise ValueError('Price must be above 0')

    def __repr__(self):
        return f'{self.__dict__}\n'

    def __str__(self):
        return f'{self.__dict__}'

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = round(value, 2)
        else:
            raise ValueError('Price must be above 0')


if __name__ == '__main__':
    item = Item(name='Item', price=100)
    print(item)
