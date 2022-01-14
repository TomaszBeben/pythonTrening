from ast import Str


x = 12
y = 2

try:
    print('START')
    print(Str(x / y)) # STOP
    print('END') # STOP
except ZeroDivisionError:
    print('nie podzielisz przez zero durniu')

print('...............')