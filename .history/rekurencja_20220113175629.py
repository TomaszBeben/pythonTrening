def func(x):
    return x * x

# print(func(5))

variable = func

print(variable(6))
print(variable)

def func2(f1, x):
    return f1(x) * x

print(func2(func, 25))

def silnia () :
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)