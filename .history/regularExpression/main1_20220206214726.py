import re

# r- przed 'stringiem' ignoruje wszeystkie znaki specjalne!!!!

pattern = r'word'
text = r'textwordtexttext'

print(pattern)
# print(re.match(r'.*' + pattern + r'.*', text))- szuka po całoscie
print(re.match(r'.*' + pattern + r'.*', text))
#  match- szuka czy wzor znajduje na poszatku textu

if re.search(pattern, text):
    print('jest')
else:
    print('nie ma')
# search szuka po calym texcie

if re.findall(pattern, text):
    print('jest')
else:
    print('nie ma')
# findall wyszukuje wszystkie

match = re.search(pattern, text)
if match:
    print(match.group)
    print(match.start)
    print(match.end)
    print(match.span)