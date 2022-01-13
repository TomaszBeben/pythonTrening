const = 1
const2 = '1'

tab = ['zero', 'jeden', 'dwa', 'trzy', [ 1, 2 ]]
# tab[1]= 'cztery'
# del tab[2]
# print(tab)
# print(len(tab))

# tab.append('cztery')
# tab.insert(2, 'jeden')
# print(tab.count('jeden'))
print(tab.index([1,2]))
tab.reverse()
print(tab)

tab2 = [1,2,3,4,5,6]
print(tab2)
tab2.clear()
print('tab2: ', tab2)