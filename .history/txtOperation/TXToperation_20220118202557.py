file = open('txtOperation\ test.txt', 'a')
# w - write
# r - read
# a - append

if file.writable():
    file.write(input('Wprowadź text: ') + '\n')  #newline - \n

file.close()

file = open('txtOperation\ test.txt', 'r')

if file.readable():
    text = file.read()
    print(text)