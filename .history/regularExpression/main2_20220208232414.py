import re

if re.match("^ca.$", 'catttt'):
    print('MATCH!')
else:
    print('DONT MATCH')