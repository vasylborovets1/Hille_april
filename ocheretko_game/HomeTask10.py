# Розширити функціонал з минулої ДЗ:
# Добавити атрибут захист герою
# Створити можливість героям використовувати спорядження для збільшення захисту чи сили.
# Зробити обмеження на кількість спорядження одним героєм ( один герою не може носити 100500 мечів і 200к щитів ).
# Створити місце де герой може купити спорядження
# Створити арени, які можуть приймати поєдинок між героями.
# Створити можливість організовувати на арені турніри між героями з великим призовим фондом.
# Всі деталі реалізації на ваш розгляд.
# Дз здавати у форматі Pull Request у вашому репозиторії.

from items import Sword, Shield
from heroes import Hero, Mage
from merchants import Merchant
from arenas import Arena

# create heroes and mages
torus = Hero(name='Torus', health=100, rank=1, power=9, defence=90)
lee = Hero(name='Lee', health=100, rank=1, power=4, defence=80)
lester = Hero(name='Lester', health=100, rank=2, power=4, defence=100)
xardas = Mage(name='Xardas', health=100, rank=1, power=10, defence=20)

# create a merchant
lagos = Merchant(name='Lagos')

# create swords and shields
gladius = Sword(name='Gladius', price=20, power_bonus=2)
knightSword = Sword(name='Knight Sword', price=30, power_bonus=3)
longSword = Sword(name='Long Sword', price=40, power_bonus=4)
runicSword = Sword(name='Runic Sword', price=50, power_bonus=5)
orcSlayer = Sword(name='Orc Slayer', price=60, power_bonus=6)
woodenShield = Shield(name='Wooden Shield', price=20, defence_bonus=20)
vikingShield = Shield(name='Viking Shield', price=30, defence_bonus=30)
guardianShield = Shield(name='Guardian Shield', price=40, defence_bonus=40)
paladinShield = Shield(name='Paladin Shield', price=50, defence_bonus=50)
aegis = Shield(name='Aegis', price=60, defence_bonus=6)

# add swords and shields to merchant's goods
lagos.goods['swords'].extend((gladius, knightSword, longSword, runicSword, orcSlayer))
lagos.goods['shields'].extend((woodenShield, vikingShield, guardianShield, paladinShield, aegis))

# create arena
arena1 = Arena(name='Arena 1', prize_fund=200)

# look at the merchant before buying equipment
print(lagos)

# buy equipment
torus.buy_equipment(lagos, gladius)
torus.buy_equipment(lagos, woodenShield)
lee.buy_equipment(lagos, longSword)
lee.buy_equipment(lagos, vikingShield)

# equip
torus.equip(gladius)
torus.equip(woodenShield)
lee.equip(longSword)
lee.equip(vikingShield)

# look at the merchant after buying equipment
print(lagos)

# this is what our heroes and arena look like before the fight
print(torus)
print(lee)
print(arena1)

# fight!
arena1.tournament(torus, lee)

# this is what our heroes and arena look like after the fight
print(torus)
print(lee)
print(arena1)

# let the mage heal our heroes if they have enough money
xardas.heal(torus)
xardas.heal(lee)

# this is what our heroes and mage look like after the healing
print(torus)
print(lee)
print(xardas)

# let's sell equipment and look at our heroes and the merchant
torus.sell_equipment(lagos, gladius)
torus.sell_equipment(lagos, woodenShield)
lee.sell_equipment(lagos, longSword)
lee.sell_equipment(lagos, vikingShield)
print(torus)
print(lee)
print(lagos)
