def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

print(gen[1])