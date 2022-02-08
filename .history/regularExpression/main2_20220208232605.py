

import re

if re.match("^[Cc]a.$", 'cat'):
    print('MATCH!')
else:
    print('DONT MATCH')