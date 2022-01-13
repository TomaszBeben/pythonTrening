wiek = input('ile masz lat?: ')
hajs = input('ile masz hajsu?: ')



if wiek >= 18 and hajs >= 50:
    print('jestes dorosły i masz hajs, wchodz')
elif wiek < 18 and wiek <=12 and hajs >= 50:
    print('małolat ale z hajsem')
