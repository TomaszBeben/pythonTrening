class Test:
    _list = []
    def add(self, arg):
        self._list.append(arg)

    def delete(self):
        if len(self._list) > 0:
            return self._list.pop(len(self._list) - 1)
        else:
            return

obj = Test()
obj.add(1)
obj.add(2)
print(obj._list)
obj.delete()
print(obj._list)

