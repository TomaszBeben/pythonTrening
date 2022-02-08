class Test:
    list = []
    def add(self, agr):
        self.list.append(arg)
    
    def delete(self, arg):
        if len(self.list) > 0:
            return self.list.pop(len(self.list) - 1)
        else:
            return

obj = Test()
obj.add(1)
obj.add(2)
print(obj.list)