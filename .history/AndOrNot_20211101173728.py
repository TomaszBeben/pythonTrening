wiek = input('ile masz lat?: ')
hajs = input('ile masz hajsu?: ')



if int(wiek) >= 18 and int(hajs) >= 50:
    print('jestes dorosły i masz hajs, wchodz')
elif int(wiek) < 18 and int(wiek) <= 12 and int(hajs) >= 50:
    print('małolat ale z hajsem')