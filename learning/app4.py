# First way
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# Second way
from ecommerce.shipping import calc_shipping
calc_shipping()

import random

for i in range(4):
    print(random.random())
    print(random.randint(20,30))
    
team = ['Abbas', 'Arvin', 'Moosavi']
leader= random.choice(team)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second= random.randint(1,6)
        return first, second
    
dice = Dice()
print(dice.roll())