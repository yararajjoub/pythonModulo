EttOrd = input("Ange ett ord: ")
bakOrd = EttOrd[::-1]

for bokstav in range(len(EttOrd)):
    bakBokstav = bakOrd[bokstav]
    print(EttOrd[bokstav], "-", bakBokstav)
