from queue import PriorityQueue


liczby = list(range(1, 100, 3))
print(liczby)

#MAP  !!!!!!!!!!!!!!!
print('=====  MAP  ======')
def f(x):
    return x * 2


mapped = map(f, liczby)

print(list(mapped))

mapped2 = map(lambda x: x * 2, liczby)

def printed(f):
    print(list(f))

printed(mapped2)

#FILTER !!!!!!!!!!!!!!!!!
print('=======  FILTER  =======')
filter1 = filter(lambda x: x > 40 , liczby)
filter2 = filter(lambda x: x % 2 == 0 , liczby)
print(list(filter1))
print(list(filter2))

print(list(filter(lambda x: x % 2 == 0, list(range(1,101)))))