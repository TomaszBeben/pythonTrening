class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print('HauHau!!')

class Wolf(Dog):
    def getVoice(self):
        print('jestem wilkiem')
        super().voice()

class Cat(Animal):
    def getVoice(self):
        print('miau...')

dog = Dog('Gucio', 13)
print(dog.name, dog.age)
dog.voice()

cat = Cat('Mruczek', 17)
print(cat.name, cat.age)
cat.getVoice()

wolf = Wolf('gerard', 20)
print(wolf.name)
wolf.getVoice()