from merchants import Merchant
from items import Sword, Shield


class Hero:

    def __init__(self, name: str, health: int or float, rank: int, power: int or float, defence: int or float):

        self.__name = name

        if 0 <= health <= 100:
            self.__health = health
        else:
            raise ValueError('Health must be between 0 and 100')

        if rank in (1, 2, 3):
            self.__rank = rank
        else:
            raise ValueError('Rank must be 1 or 2 or 3')

        if 0 <= power <= health * 0.1:
            self.__power = power
        else:
            raise ValueError('Power must be between 0 and 10% health')  # power boost may apply when sword is equipped

        if 0 <= defence <= 100:
            self.__defence = defence
        else:
            raise ValueError('Defence must be between 0 and 100')  # defence boost may apply when shield is equipped

        self.__money = 100

        self.__inventory = {
            'swords': [

            ],
            'shields': [

            ]
        }

        self.__sword = None  # boosts power when equipped (when is not None)

        self.__shield = None  # boosts defence when equipped (when is not None)

    def __str__(self):
        return (f'Name: {self.name}\nClass: {self.__class__.__name__}\nAttributes: health: {self.health}, '
                f'rank: {self.rank}, power: {self.power}, defence: {self.defence}, money: {self.money}\n'
                f'Sword: {self.sword}\nShield: {self.shield}')

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.__health = round(value, 2)

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value: int):
        if value > 3:
            value = 3
        elif value < 1:
            value = 1
        self.__rank = value

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value > self.health * 0.1:
            self.__power = value
        elif value < 0:
            value = 0
        if self.sword is not None:
            self.__power = round(value, 2) + self.sword.power_bonus
        else:
            self.__power = round(value, 2)
        # power boost may apply when sword is equipped
        # power goes back to its original value when sword is unequipped
        # so make sure the sword is unequipped if you face an unexpected result after setting a new power value

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        if self.shield is not None:
            self.__defence = round(value, 2) + self.shield.defence_bonus
        else:
            self.__defence = round(value, 2)
        # defence boost may apply when shield is equipped
        # defence goes back to its original value when shield is unequipped
        # so make sure the shield is unequipped if you face an unexpected result after setting a new defence value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if value < 0:
            value = 0
        self.__money = round(value, 2)

    @property
    def inventory(self):
        return self.__inventory

    @property
    def sword(self):
        return self.__sword

    @property
    def shield(self):
        return self.__shield

    def buy_equipment(self, merchant: Merchant, item: Sword or Shield):
        if (item in merchant.goods['swords'] or item in merchant.goods['shields']) and item.price <= self.money:
            if item.__class__ == Sword and len(self.inventory['swords']) < 3:
                self.money -= item.price
                merchant.money += item.price
                merchant.goods['swords'].remove(item)
                self.inventory['swords'].append(item)
            elif item.__class__ == Shield and len(self.inventory['shields']) < 3:
                self.money -= item.price
                merchant.money += item.price
                merchant.goods['shields'].remove(item)
                self.inventory['shields'].append(item)

    def sell_equipment(self, merchant: Merchant, item: Sword or Shield):
        if (item in self.inventory['swords'] or item in self.inventory['shields']) and item.price <= merchant.money:
            if item.__class__ == Sword:
                if item is self.sword:
                    self.unequip(self.sword)
                merchant.money -= item.price
                self.money += item.price
                self.inventory['swords'].remove(item)
                merchant.goods['swords'].append(item)
            elif item.__class__ == Shield:
                if item is self.shield:
                    self.unequip(self.shield)
                merchant.money -= item.price
                self.money += item.price
                self.inventory['shields'].remove(item)
                merchant.goods['shields'].append(item)

    def equip(self, item: Sword or Shield):
        if item in self.inventory['swords']:
            if self.sword is not None:
                self.unequip(self.sword)
            self.__sword = item
            self.__power += item.power_bonus
        elif item in self.inventory['shields']:
            if self.shield is not None:
                self.unequip(self.shield)
            self.__shield = item
            self.__defence += item.defence_bonus

    def unequip(self, item: Sword or Shield):
        if self.sword is item:
            self.__sword = None
            self.power -= item.power_bonus
        elif self.shield is item:
            self.__shield = None
            self.defence -= item.defence_bonus

    def hit(self, enemy):
        if enemy is self:
            print('Cannot fight against myself!')
            return
        elif self.rank != enemy.rank:
            print(f'{self.name} can fight with the enemy of the same rank only')
            return
        elif enemy.health <= 5:
            print(f'{enemy.name} cannot fight right now!')
            return
        elif self.health <= 5:
            print(f'{self.name} cannot fight right now!')  # because it would be unfair if hero with health <5 could hit
            # the enemy and the enemy would not be able to hit the hero
            return
        damage = self.power * ((100 - enemy.defence * 0.1) / 100)
        enemy.health -= damage
        if enemy.sword is not None:
            if (enemy.power - enemy.sword.power_bonus) > enemy.health * 0.1:
                enemy.power = enemy.health * 0.1
        else:
            if enemy.power > enemy.health * 0.1:
                enemy.power = enemy.health * 0.1
        if enemy.health < 5:
            print(f'{self.name} won!')
            enemy.health = 5
            enemy.power = enemy.health * 0.1
            self.money += enemy.money
            enemy.money -= enemy.money


if __name__ == '__main__':
    hero = Hero(name='Hero', health=100, rank=1, power=9, defence=90)
    print(hero)
