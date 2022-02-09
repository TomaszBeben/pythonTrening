# * - pozwala na wystapienie n razy przy zznaku przy ktorym sie znajduje(moze tez sie nie pojawic)
# + - pozwala na wystapienie n razy przy zznaku przy ktorym sie znajduje(musi pojawic sie przynajmniej raz)
# ? - pozwala na wystapienie znaku jeden raz lub zero razy
# {2,4} - znak musi sie pojawic od... do...

import re

if re.match('^[A-Z][a-z]*$', 'Ala'):
    print('GIT')
else:
    print('hujnia')
print('-----------------')

if re.match('^[A-Z][a-z]*$', 'Ala'):
    print('GIT')
else:
    print('hujnia')
print('-----------------')

if re.match('^[A-Z][a-z]+$', 'Ala'):
    print('GIT')
else:
    print('hujnia')
print('-----------------')

if re.match('^[A-Z][a-z]?[A-Z]', 'Ala'):
    print('GIT')
else:
    print('hujnia')
print('-----------------')

if re.match('^[A-Z][a-z]{3,6}$', 'Alan'):
    print('GIT')
else:
    print('hujnia')