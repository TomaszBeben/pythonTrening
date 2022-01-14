x = 12
y = 0

try:
    lista = []
    print(lista[1])
    print(x + '!')
    print(x / y) # STOP
    print('END') # STOP
except (ZeroDivisionError, TypeError):
    print('błąd!!')
except:
    print('kazdy inny błąd')
finally:
    print('finally wykonuje sie zawsze')

print('...............')