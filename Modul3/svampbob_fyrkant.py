ettOrd = input('Ange ett ord: ')
nyttOrd = ''

for bokstav in range(len(ettOrd)):  # index /Position
    if bokstav % 2 == 0:
        nyttOrd += ettOrd[bokstav].lower()
    else:
        nyttOrd += ettOrd[bokstav].upper()
print(nyttOrd)
