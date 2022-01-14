from ast import Str
from tokenize import String


x = 12
y = 2

try:
    print('START')
    print(String(x / y)) # STOP
    print('END') # STOP
except ZeroDivisionError:
    print('nie podzielisz przez zero durniu')

print('...............')