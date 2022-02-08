wyrazenia regularne
. - dowolny znak
^ - slowo musi zaczynac sie od nastepujacego znaku
$ - dokładnie przed tym nakiem koczy sie slowo

import re

if re.match("^[Cc]a.$", 'cat'):
    print('MATCH!')
else:
    print('DONT MATCH')