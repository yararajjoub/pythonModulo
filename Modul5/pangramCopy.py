"""
- Ett pangram är en mening som använder alfabetets alla bokstäver, minst en gång vardera.
- Skriv en funktion is_pangram som tar en text som argument och som avgör huruvida texten är ett pangram.
- Funktionen ska returnera ett värde av typen bool.
- Funktionen ska använda det engelska alfabetet och kunna hantera både små och stora bokstäver.
"""

""" 
alfabeter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_pangram(meningLista):
    #ispangra = False
    mening = ''
    meninglst = []
    for alfabeter in range(len(meningLista)):
        if alfabeter in meninglst:
            meninglst += alfabeter
            ispangra= True
        else:
            print('hej')
            ispangra = False
    return ispangra
"""

#Funktion is_pangram(text):
#alphabet = set("abcdefghijklmnopqrstuvwxyz")  # Skapa ett set med alla bokstäver i alfabetet
#lowercase_text = text.lower()  // Konvertera texten till gemener
""" 
För varje tecken i lowercase_text:
Om tecken är en bokstav:
Ta bort tecken från alphabet

Om alphabet är tomt:
Returnera True  // Alla bokstäver finns i texten (pangram)
Annars:
Returnera False  // Minst en bokstav saknas i texten (inte ett pangram)
"""

def is_pangram(textLista):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lowercase_text = textLista.lower()
    for item in lowercase_text:
        if item in alphabet:
            alphabet.remove(item)
    if len(alphabet) == 0:
        return True
    else:
        return False


text = 'This is just any text.'
if is_pangram(text):
    print('The text is a pangram.')      # This will be printed
else:
    print('The text is not a pangram.')
