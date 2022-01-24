liczby = list(range(1, 100, 3))
print(liczby)

#map

def f(x):
    return x * 2


mapped = map(f, liczby)

print(list(mapped))

mapped2 = map(lambda x: x * 2, liczby)