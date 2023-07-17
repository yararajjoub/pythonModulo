"""
ordE = input('skriv ett ord:')

vokaler = 'aouåeiyäö'
# Iterara över alla bokstäver i ordet, genom for-sats
for bokstav in ordE:
    # kollar om aktuella bokstaven finns i stringen vokaler
    if bokstav.lower() in vokaler: #gör om boksatven till små
        print('*', end='')  # if true så skriv ut en stjärna
    else:
        print(bokstav, end='')

print()
"""

""" 
ordE = input('Skriv ett ord: ')

vokaler = 'aouåeiyäö'

# Använd replace() för att byta ut vokalerna mot asterisker
ordE = ordE.replace('a', '*')
ordE = ordE.replace('o', '*')
ordE = ordE.replace('u', '*')
ordE = ordE.replace('å', '*')
ordE = ordE.replace('e', '*')
ordE = ordE.replace('i', '*')
ordE = ordE.replace('y', '*')
ordE = ordE.replace('ä', '*')
ordE = ordE.replace('ö', '*')

print(ordE)

"""
"""
name = input('Ange namn(för & efter namn): ')
# Hitta första mellanslaget i namnet, använd funktionen find
position = name.find(' ')  # Dvs positionen där mellan slaget finns
print(position)  # kommer output: 5 (indexPosition)
# Slicing = att plocka en del av stringen, i detta fallet (efternamn)
efternamn = name[position:]  # Gå igenom positionen och ända fram till slutet
print(efternamn)  # har fått med mellanslaget också, vilket är fel därför ändrar vi
efternamn = name[position+1:]
print(efternamn)
print(f'The name is: {efternamn}, {name}.')


 """

# Avstavning
EttOrd = input('Skriv ett ord: ')
nyOrd = ''  # String för att lagra in det nya ordet

for i in range(len(EttOrd)-1):  # Iterera över alla positioner/index i ordet, förutom den sista
    nyOrd = nyOrd + EttOrd[i] + '_'  # Lägg till bokstaven på den givna indexet och ett streck

nyOrd = nyOrd+EttOrd[-1]  # Lägg till den sista bokstaven
print(nyOrd)  # Skriv ut resultatet i den nya stringen

