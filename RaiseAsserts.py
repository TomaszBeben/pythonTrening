def dzielenie(x, y):
    assert y != 0, 'Y == 0'
    if y == 0:
        raise ZeroDivisionError('dzielenie przez 0')
    print(x / y)

try:
    dzielenie(2, 0)
except ZeroDivisionError:
    print('0 0 0')