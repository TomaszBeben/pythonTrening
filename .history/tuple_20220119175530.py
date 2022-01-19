from xml.dom.minidom import Element


krotka = (2, 4, 8, 16, 32, 64, 128)

print(krotka[1])
print(krotka)

#krotka[0] = 1 - tuple is not mutable!

print('Elementów: ', krotka.count(2))
print('index: ', krotka.index(64))
print('liczba elementów: ' ,len(krotka))


# wycinki
print('\nwycinek:')
print(krotka[0:3])
print(krotka[2:3])