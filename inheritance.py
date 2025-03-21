class Animal:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass


dog = Dog('Puppy')
dog.introduce()
# Hi, I'm Puppy

