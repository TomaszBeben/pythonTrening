lista = list(range(1, 11))

print(lista)

nowa = [i * 2 for i in lista]

print('stara: ', lista)
print('nowa: ', nowa)

nowa2 = [i + 2 for i in lista if i % 2 == 1]
print( 'nowa2: ' ,nowa2)

# string formatter

arg = ['Tomek', 30]
text = 'elo elo, mam na imie {0} i mam {1} lat.'.format(arg[0], arg[1])

print(text)