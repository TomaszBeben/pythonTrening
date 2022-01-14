from ast import Str
from tokenize import String


x = 12
y = 2

try:
    print(x + '!')
    print(x / y) # STOP
    print('END') # STOP
except ZeroDivisionError:
    print('nie podzielisz przez zero durniu')
except TypeError:
    print('błąd typu danych')

print('...............')