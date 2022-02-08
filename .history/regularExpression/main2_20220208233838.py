# wyrazenia regularne
# . - dowolny znak
# ^ - slowo musi zaczynac sie od nastepujacego znaku
# $ - dokładnie przed tym nakiem koczny sie slowo
# [] - klasa mozliwych znakow
# [A-Z] - klasa duzych znakow
# [A-Za-z] -tylko litery(duze i małe)
# [0-9] - tylko liczby
# [^] - symbol ^ w przedziale robi negacje czyli [^A-Z] nie moze byc duzych liter

import re

if re.match('^[yY]ear[-=+:][0-9][0-9][0-9][0-9]$', 'Year-2022'):
    print('MATCH!')
else:
    print('DONT MATCH')