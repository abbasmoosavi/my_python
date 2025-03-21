class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
        
point1 = Point(20,30)
print(point1.x)
# 20
# /////
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name}.")

person = Person(input('name: '))
person.talk()
# name: Abbas
# Hi, I'm Abbas