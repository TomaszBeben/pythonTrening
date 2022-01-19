from xml.dom.minidom import Element


krotka = (2, 4, 8, 16, 32, 64, 128)

print(krotka[1])
print(krotka)

#krotka[0] = 1 - tuple is not mutable!

print('Elementów: ', krotka.count())