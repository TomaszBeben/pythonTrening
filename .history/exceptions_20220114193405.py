x = 12
y = 0

try:
    print('START')
    print(x / y) # STOP
    print('END') # STOP
except ZeroDivisionError:
    print('nie podzielisz przez zero durniu')

print('...............')