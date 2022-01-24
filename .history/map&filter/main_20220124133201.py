liczby = list(range(1, 100, 3))
print(liczby)

#MAP  !!!!!!!!!!!!!!!

def f(x):
    return x * 2


mapped = map(f, liczby)

print(list(mapped))

mapped2 = map(lambda x: x * 2, liczby)

def printed(f):
    print(list(f))

printed(mapped2)

#FILTER !!!!!!!!!!!!!!!!!

filter1 = filter(lambda x: x > 40 , liczby)
pr