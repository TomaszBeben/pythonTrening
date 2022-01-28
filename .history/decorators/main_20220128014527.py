def decorator(f):
    def wrapper():
        print("-------")
        f()
        print("-------")
    return wrapper

def hello():
    print('HELLO')

# decorator(hello)
hello = decorator(hello)
hello()

@decorator
def nara():
    print('nara ziomek')