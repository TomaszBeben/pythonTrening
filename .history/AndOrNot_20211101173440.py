wiek = input('ile masz lat?: ', int())
hajs = input('ile masz hajsu?: ', int())



if wiek >= 18 and hajs >= 50:
    print('jestes dorosły i masz hajs, wchodz')
elif wiek < 18 and wiek <=12 and hajs >= 50:
    print('małolat ale z hajsem')