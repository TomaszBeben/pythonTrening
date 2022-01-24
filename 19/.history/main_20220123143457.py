file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
file.close()
print(text)

# def count(txt, sign):
#     counter = 0
#     for z in txt:
#         if z == sign:
#             counter += 1
#     return counter

# print(count(text.lower(), 'a'))