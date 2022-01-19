lista = list(range(1, 11))

print(lista)

nowa = [i * 2 for i in lista]

print('stara: ', lista)
print('nowa: ', nowa)

nowa2 = [i + 2 for i in lista if i % 2 == 1]
print( 'nowa2: ' ,nowa2)

# string forrmattetr