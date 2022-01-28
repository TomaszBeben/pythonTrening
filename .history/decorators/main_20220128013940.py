def decorator(f):
    def wrapper():
        print("-------")
        f()
        print("-------")
    return wrapper

def hello():
    print('HELLO')
    
decorator(hello)