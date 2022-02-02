class Person:
    def __init__(self, name, surname,age):
        self.name = name
        self.age = age
        self.surname = surname

    # name = "Tomek"
    # surname = "Beben"

    def introduce(self, welcome = 'Elo'):
        return  welcome + ", mam na imie " + self.name + " " + self.surname + " i mam " + str(self.age) + ' lat'

obj = Person('tome', 'beben', 29)
print(obj.name)
print(obj.surname)
print(obj.introduce())

# obj2 = Person()
# print(obj2.introduce())
# print(obj2.introduce('Siema'))