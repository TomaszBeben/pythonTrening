from random import randint

los = randint(1, 100)
odp = -1
i = 0

print('wylosuj liczbe od 1 - 10')
while odp != los:
    i =+ 1
    odp = int( input( 'podaj liczbe: ' ) )
    if odp > los:
        print('za duzo')
    elif odp == los:
        print('Gratulacja!! wlosowana liczba to: ', los)
    else:
        print('za mało')