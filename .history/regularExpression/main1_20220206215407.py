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

matching = re.search(pattern, text)
if matching:
    print(matching.group())
    print(matching.start())
    print(matching.end())
    print(matching.span())
    
text2  = re.sub(pattern, r'something', text)
print(text2)