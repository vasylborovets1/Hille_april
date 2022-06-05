from heroes import Hero, Mage
from random import choice


class Arena:

    def __init__(self, name: str, prize_fund: int):
        self.__name = name
        if prize_fund >= 100:
            self.__prize_fund = prize_fund
        else:
            raise ValueError('Prize fund must be 100 and higher')

    def __str__(self):
        return f'{self.name}, Prize fund: {self.prize_fund}'

    @property
    def name(self):
        return self.__name

    @property
    def prize_fund(self):
        return self.__prize_fund

    @prize_fund.setter
    def prize_fund(self, value):
        if value < 100:
            value = 100
        self.__prize_fund = value

    def tournament(self, fighter1: Hero or Mage, fighter2: Hero or Mage):
        if self.prize_fund < 100:
            print(f'This arena is temporarily unavailable. Choose another one')
            return
        print(f'{fighter1.name} VS {fighter2.name}')
        winner = None
        looser = None
        who_hits_first = choice((fighter1, fighter2))
        if who_hits_first == fighter1:
            while True:
                fighter1.hit(fighter2)
                fighter2.hit(fighter1)
                if (fighter1.health <= 5 or fighter2.health <= 5 or fighter1 is fighter2 or
                        fighter1.rank != fighter2.rank):
                    break
                if fighter1.health == fighter2.health:
                    print('There are no winners in this battle')
                    return
                elif fighter1.health > fighter2.health:
                    winner = fighter1
                    looser = fighter2
                else:
                    winner = fighter2
                    looser = fighter1
        else:
            while True:
                fighter2.hit(fighter1)
                fighter1.hit(fighter2)
                if (fighter1.health <= 5 or fighter2.health <= 5 or fighter1 is fighter2 or
                        fighter1.rank != fighter2.rank):
                    break
                if fighter1.health == fighter2.health:
                    print('There are no winners in this battle')
                    return
                elif fighter1.health > fighter2.health:
                    winner = fighter1
                    looser = fighter2
                else:
                    winner = fighter2
                    looser = fighter1
        if winner is not None and looser is not None:
            winner.money += self.__prize_fund * 0.8
            looser.money += self.__prize_fund * 0.2
            self.__prize_fund = 0
            print(f'Winner: {winner.name}, looser: {looser.name}')


if __name__ == '__main__':
    arena = Arena(name='Arena', prize_fund=100)
    print(arena)
