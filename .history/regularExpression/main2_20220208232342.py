import re

if re.match("^ca.$", 'cattttt'):
    print('MATCH!')
else:
    print('DONT MATCH')