wiek = input('ile masz lat?: ')
hajs = input('ile masz hajsu?: ')



if wiek >= int(18) and hajs >= int(50):
    print('jestes dorosły i masz hajs, wchodz')
elif wiek < int(18) and wiek <=int(12) and hajs >= int(50):
    print('małolat ale z hajsem')