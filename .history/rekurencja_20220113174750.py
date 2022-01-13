def func(x):
    return x * x

# print(func(5))

variable = func

print(variable(6))
print(variable)

def func(f1, x):
    return f1(x)


