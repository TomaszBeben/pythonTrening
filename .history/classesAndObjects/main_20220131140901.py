class Person:
    name = "Tomek"
    surname = "Beben"

    def introduce(self):
        return "Elo, mama na imie" + self.name + " " + self.surname

obj = Person()
print(obj.name)
print(obj.surname)
print(obj.introduce())
