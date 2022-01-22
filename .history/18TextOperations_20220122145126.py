print(', '.join(['a', 'b', 'c'])) # łączy

print('Elo World'.replace('Elo', 'Witaj'))# zamienia

print('to jest zdanie'.startswith('to')) #true
print('to jest zdanie'.startswith('To')) #false

print('to jest zdanie'.endswith('zdanie')) #true
print('to jest zdanie'.endswith('ie')) #true
print('______________________')
print('t' in 'to jest zdanie') #true
print('w' in 'to jest zdanie') #false

print('to jest zdanie'.upper())
print('to jest zdanie'.lower())

print('___________________________')

list = [10, 15, 20, 25, 30,]
# list = [10, 20, 30,]

if all([i % 2 == 0 for i in list]):
    print('wszystko parzyste')
else:
    print('jest tam cos nieparzystego')

if any([i % 2 == 0 for i in list]):
    print('przynajmniej 1 parzysta')
else:
    print('0 parzystych')

for i in enumerate(list):
    print(i)