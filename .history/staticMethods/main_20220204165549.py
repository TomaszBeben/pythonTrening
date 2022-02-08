from tokenize import PseudoExtras


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('my name is ' + self.name)

    @classmethod
    def new_person(cls, name):
        return cls(name)
    
person1 = Person('Tomek')
person1.introduce()

person2 = Person.new_person('Ziomek')
person2.introduce()