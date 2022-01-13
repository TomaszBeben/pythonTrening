print('Funkcje')

def first_function(arg):
    print(arg)

first_function('elo')
first_function('elo2')
first_function('elo3 ')

def dodawanie(a):
    print(a + 1)

dodawanie(1)

def dodawanie(a, b = 0,): # deklaracja argumentu pozwala na opcjonalne podanie argumentu
    c = a + b
    print(c, 'asasdsad')

# dodawanie(2,3)
# dodawanie(2)

dodawanie(2,4)