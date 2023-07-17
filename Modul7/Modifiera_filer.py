"""
There are two rules of thumb when handling files:
▶ Always use the with statement to open and close files
▶ Keep the files open as briefly (kort) as possible, minska risken för error

We will also introduce command line arguments
▶ An alternative to the input() function, för att ta emot data från user

The process of changing (modify) the files :
▶ read −→ modify −→ write
"""


# Exempel för att ändra en fil


def pig_latin(word):
    if word[0].lower() in 'aeiouy':  # starts with a vowel
        return word + 'way'
    else:
        for i, letter in enumerate(word):  # för att iterera över bokstäverna i ordet + deras position (i-index, letter)
            if letter.lower() in 'aeiouy':  # find first vowel
                return word[i:] + word[:i] + 'ay'
    return word  # return ordet if no cond = True


# "Banana"-String, och i är 2, skulle word[i:] bli "nana".
# "banana"-Sting, och i är 2, skulle word[:i] bli "ba" (inkluderar inte 2)
" Exempel på output av pig_latin(word) func:"
# Input 'word' = tomat
# omat, to, ay
# return word = omattoay

# läser från en fil och ändrar format (call pig_latin()) och sen skriv tillbaka den i filen
fileName = input('Enter file name: ')
with open(fileName) as filen:  # as default kommer filen att läsas
    lines = filen.readlines()  # read the content into a list, lista av strängar varje rad
# filen stängs automatisk här

new_lines = []  # An empty list of the NEW lines to store data in
for line in lines:  # Iterera från lines som vi tidigare har läst in från filen
    nl = '' " för varje rad skapar vi ny sträng "
    for wd in line.split():  # för varje ord i raden, vi skapar en lista av dessa ord -- ex lista: ['hej', 'world']
        nl += pig_latin(wd) + ' '
        # varje ord skickar in till fun pig_latin för att översätta och addera ordet + '' till aktuella raden
    new_lines.append(
        nl + '\n')  # efter vi har gjort tidigare så lägger vi den nya raden i listan över rader, med manuellt rad brytning (filen)

# öppnar filen igen, pga regler till fil-hantering ovan
# vi gör skrivning här till slutet
with open(fileName, 'w') as f:
    for line in new_lines:
        f.write(line)

""" File Operation """
nbr_char = 2
chars = f.read(nbr_char)
# vi läser visst antal karaktärer i filen, n= antal Char, default antal = 1 som kommer att läsas
s = 'strängen som vi vill infoga i filen'
nbr_char = f.write(s)  # output: writes the 's' to the file, returns the nbr of characters written

# vi kan även printa till filen istället för standard output
print('printa denna strängen till filen', file=f)  # mindre vanligare, vi använder write istället

import sys
""" 
argv[0] -- contains the name of current python program
argv[1:] -- contains any command line arguments passed to the program
"""
print('program: ', sys.argv[0])  # the name fo the program
for arg in sys.argv[1:]:
    print('argument: ', arg)
