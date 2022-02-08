import re

# r- przed 'stringiem' ignoruje wszeystkie znaki specjalne!!!!

pattern = r'word'
text = r'wordtextwordtexttext'

print(pattern)
print(re.match(r'.*' + pattern + r'.*', text))