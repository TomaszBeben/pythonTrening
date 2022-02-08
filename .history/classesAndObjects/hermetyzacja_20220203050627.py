class Test:
    list = []
    def add(self, arg):
        self.list.append(arg)

    def delete(self):
        if len(self.list) > 0:
            return self.list.pop(len(self.list) - 1)
        else:
            return

obj = Test()
obj.add(1)
obj.add(2)
print(obj.list)
obj.delete()
print(obj.list)