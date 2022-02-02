class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print('HauHau!!')

dog = Dog('Gucio', 13)
print(dog.name, dog.age)