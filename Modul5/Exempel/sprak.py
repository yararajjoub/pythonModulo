#tar in en text och returnerar texten översatt till rövarspråket.
Konsonanter = 'bcdfghjklmnpqrstvwxz'
""" 
#Skapa sträng och översätt steg för steg
def translate(original):
    translation = ''
    for bokstav in original:
        if bokstav in Konsonanter:
            translation += bokstav + 'o' + bokstav
        else:
            translation += bokstav
    return translation


text = input('Ange en text: ')
oversattning = translate(text)
print(oversattning)
"""
#hantera flera ord och hantera även stora bokstäver
def translate(original):
    translation = ''
    for bokstav in original:
        if bokstav.lower() in Konsonanter:
            translation += bokstav + 'o' + bokstav.lower()
        else:
            translation += bokstav
    return translation


text = input('Ange en text: ')
oversattning = translate(text)
print(oversattning)
