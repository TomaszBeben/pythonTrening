class Person:
    name = "Tomek"
    surname = "Beben"

    def introduce(self, welcome = 'Elo'):
        return  welcome + ", mam na imie " + self.name + " " + self.surname

obj = Person()
print(obj.name)
print(obj.surname)
print(obj.introduce())

obj2 = Person()
obj2.name = 'Ziomek'
obj2.surname = 'Ziomek'
print(obj2.introduce())
print(obj2.introduce('Siema'))