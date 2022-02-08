wyrazenia regularne
. - dowolny znak
^ - slowo musi zaczynac sie od nastepujacego znaku
$ - dokładnie przed tym nakiem koczny sie slowo
[] - klasa mozliwych znakow

import re

if re.match("^[Cc]a.$", 'cat'):
    print('MATCH!')
else:
    print('DONT MATCH')