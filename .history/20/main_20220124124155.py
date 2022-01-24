def func(f, num):
    return f(num)

print(func(lambda x: x * x, 3))

def square(x):
    return x * x

print(square(5))

result = lambda x: x * x
print(result)