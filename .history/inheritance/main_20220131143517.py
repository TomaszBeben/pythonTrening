class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print('HauHau!!')

class Wolf(Dog):
    

class Cat(Animal):
    def getVoice(self):
        print('miau...')

dog = Dog('Gucio', 13)
print(dog.name, dog.age)
dog.voice()

cat = Cat('Mruczek', 17)
print(cat.name, cat.age)
cat.getVoice()