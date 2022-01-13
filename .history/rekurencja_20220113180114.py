def func(x):
    return x * x

# print(func(5))

variable = func

print(variable(6)) # 36
print(variable) # <function func at 0x0000021EE042B640>

def func2(f1, x):
    return f1(x) * x

print(func2(func, 5)) # 125

def silnia(x) :
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(12355)) # 120