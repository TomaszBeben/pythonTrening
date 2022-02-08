class Test:
    __list = []
    __list = []
    def add(self, arg):
        self.__list.append(arg)

    def delete(self):
        if len(self.__list) > 0:
            return self.__list.pop(len(self.__list) - 1)
        else:
            return

obj = Test()
obj.add(1)
obj.add(2)
# print(obj.__list)
obj.delete()
# print(obj.__list)
print(obj.__list)

