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

word = 'text'

upperWord = word.upper()
print(upperWord)