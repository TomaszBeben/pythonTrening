from ast import Str
from tokenize import String


x = 12
y = 0

try:
    print(x + '!')
    print(x / y) # STOP
    print('END') # STOP
except (ZeroDivisionError, TypeError):
    print('blad')

print('...............')