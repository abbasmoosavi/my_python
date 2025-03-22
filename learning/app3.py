import converters
print(converters.kg_to_lbs(82))

# second way to import modules
from converters import lbs_to_kg
print(lbs_to_kg(40))

# Find max number of array using module
from utils import find_max
print('Enter 5 numbers:')
numbers=[]
i=0
while i < 5:
    number = int(input('> '))
    numbers.append(number)
    i+=1
find_max(numbers)