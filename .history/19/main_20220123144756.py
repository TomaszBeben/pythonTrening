file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

def count(txt, sign):
    counter = 0
    for z in txt:
        if z == sign:
            counter += 1
    return counter

print(count(text.lower(), 'a'))
print(count(text.lower(), 'z'))

print(len(text))

for i in 'abcdefghijklmnoprstuwxyz':
    ile= count(text.lower(), i)
    procent = 100 * ile / len(text)
    print('{0} - {1} - {2} %'.format(i.upper(), ile, round(procent, 2)))

