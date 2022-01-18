file = open('txtOperation\ test.txt', 'w')

if file.writable():
    file.write(input('Wprowadź text: ') + '\n')  #newline - \n

file.close()