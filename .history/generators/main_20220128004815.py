def gen():
    i = 0
    while i <= 5:
        yield i
        i += 1

for i in gen():
    print(i)

print(list(gen()))