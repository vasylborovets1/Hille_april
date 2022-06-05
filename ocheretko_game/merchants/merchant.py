class Merchant:

    def __init__(self, name):
        self.__name = name
        self.__money = 1000
        self.goods = {
            'swords': [

            ],
            'shields': [

            ]
        }

    def __str__(self):
        return f'Name: {self.name}\nClass: {self.__class__.__name__}\nMoney: {self.__money}\nGoods: {self.goods}'

    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if value < 0:
            value = 0
        self.__money = round(value, 2)


if __name__ == '__main__':
    merchant = Merchant('Merchant')
    print(merchant)
