def dzielenie(x, y):
    if y == 0:
        raise ZeroDivisionError('dzielenie przez 0')
    print(x / y)
dzielenie(2, 0)