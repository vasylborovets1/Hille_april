from heroes import Hero


class Mage(Hero):

    def heal(self, hero):
        if hero is self:
            print('Cannot heal myself!')
            return
        elif hero.health >= 100:
            print(f'{hero.name} has maximum health points already')
            return
        elif hero.health < 100 and hero.money >= (100 - hero.health):
            heal_points = (100 - hero.health)
            hero.health += heal_points
            hero.power = hero.health * 0.1
            hero.money -= heal_points
            self.money += heal_points
            # restores health and power to their maximum possible values (health = 100 and power = 10% of health)
            # not depending on what they were like upon the initial hero creation
            # (example: hero created "not feeling well" with health = 80 and power = 7,
            # then health dropped to 50 and power to 5 after a fight,
            # so "heal" restores them to 100 and 10 respectively)
            # note that additionally power boost may apply when a sword is equipped


if __name__ == '__main__':
    mage = Mage(name='Mage', health=100, rank=1, power=10, defence=20)
    print(mage)
