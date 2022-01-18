dictionary = {
    1: 'poniedziałek',
    2: 'wtorek',
    3: 'sroda',
}

print(dictionary[1])
dictionary[4] = 'czwartek'
print(dictionary)

print('petla: ')
for l in dictionary.values():
    print(l)
print('\n\n')
print('________')
print(dictionary.pop(1))
print(dictionary)