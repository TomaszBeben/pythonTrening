file = open('txtOperation\ test.txt', 'a')
# w - write
# r - read
# a - append

if file.writable():
    file.write(input('Wprowadź text: ') + '\n')  #newline - \n

file.close()

file = open('txtOperation\ test.txt', 'r')

if file.readable():
    print('Zawartość pliku')
    for l in file:
        print(l)
