class Person:
    name = "Tomek"
    surname = "Beben"

    def introduce(self):
        return "Elo, mama na imie" + self.name

obj = Person()
print(obj.introduce)