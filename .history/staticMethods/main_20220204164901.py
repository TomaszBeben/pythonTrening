from tokenize import PseudoExtras


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('my name is' + self.name)



person1 = Person('Tomek')
person1.introduce()