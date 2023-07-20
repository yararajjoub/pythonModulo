# Container = datatyp som innehåller en annan obj, container supportar operator in, och tillåter
# iteration över elementen i container

"""
 Sekvenser är container: bla, str-string, list, tuple

 * INTE alla containers är sekvenser:
 EX: set, dict inbyggd typer som lagrar object i
   - Set = lagrar Osorterad collection av UNIKA elements
   - Dict = lagrar collection av Key-Value par med unika KEYS "maps"
 * Datatypen set är optimerad för snabb medlemskapstestning.
   Tiden det tar att testa är oberoende av hur många element som finns i set:et.

*** gemensamma egenskaper ***
    - skapas från literal och sekvenser, in operator och hur man itererar
"""

# Att skapa set och dict från literaler
enSet = {'one', 'two', 'three'}
enDikt = {'en': 1, 'två': 2, 'tre': 3}

# Att skapa set och dict från sekvenser:
minSet = ['eins', 'zwei', 'drcsd']
de = set(minSet)  # skapar set

numeri = [('uno', 1), ('due', 2), ('tre', 3)]  # Denna är en lista
it = dict(numeri)  # skapar dict
"""  Man kan också skapa en dict från en lista, men vi behöver också då nycklar och value till den """
" Man kan skapa dictionaries using keywords ex: "
es = dict(uno=1, två=2, tre=3, fyra=4)  # nyckelord kommer tolkas som strängar och heltal är våra values,
# bara enkel sträng som ett ord
print(es)  # output: {'uno': 1, 'två': 2, 'tre': 3, 'fyra': 4}

" Att skapa tomma dictionaries and sets "
empty = {}  # empty dictionary
void = dict()  # empty dictionary #output {}
nothing = set()  # empty set # output:  set()
# print(nothing) output:  set()


" Dictionaries can be created from two sequences using zip() "  # man kan använda (range-obj eller listor eller tupler)
nummer = ['ett', 'två', 'tre']
numbers = dict(zip(nummer, range(1, 4)))  # range object from 1-4
print(numbers)  # output: {'ett': 1, 'två': 2, 'tre': 3} Vi får key och värde par

" Set & Dictionaries comprehension "
"range =  0 till 3 (dvs. [0, 1, 2, 3])."
settet = {x ** 2 for x in range(4)}  # {0, 1, 4, 9} x upphöjt till två
dictionarie = {x: 2 ** x for x in range(4)}  # output: {0:1, 1:2, 2:4, 3:8,}

"""  I Sets och Dictionaries kan man använda operator in & not in för att kontrollera om de innehåller en visst element 
OutPut bli True, False """

" Set är muterbar dvs man kan lägga till eller ta bort element"
# vi kan lägga till eller ta bort samma element och inget fel inträffar, utan Nothing happens
m = {2, 4, 6}
m.add(8)  # {8, 2, 4, 6}
m.add(6)  # nothing happens
m.discard(4)  # {8, 2, 6}
m.remove(2)  # {8, 6}
m.discard(7)  # nothing happens
# m.remove(7)     # KeyError: 7
""" 
För att undvika felet kan du använda metoden discard() istället, eftersom den inte kastar något undantag om elementet 
inte finns i mängden. Om elementet redan finns i mängden, tas det bort; annars gör discard() ingenting.
"""
m.pop()  # draw a random.txt element from m # output: {6} eller {2,4,6} som i original
# m.clear()       # removes all the elements
print(m)

" Vi kan använda frozenset som är icke-muterbar version av set "


" iterera över elem i set"
en = {'one', 'two', 'three'}
for number in en:
    print(number, end=' ')
# output: one three two # därför att det printas random.txt ordning, man garanterar inte ordningen som det är, inget error
" En Set är osorterad type "
"""
# fast medlemskap testning
"följande sättet för att testa sekvensen tar en gång mer än själva sekvensen"
c = input('\nSkriv ett ord: ')
if c in 'aeiouy':
    pass  # do something

" membership testing in a set/(frozenset) always takes constant time "
if c in frozenset('aeiouy'):
    pass  # do something
# bättre algoritm för att testa värdet av c finns bland 'vokalerna', gör om strängen till frozenset

"""
" Operations Dictionary "
frns = {'un': 1, 'duex': 2, 'trois': 3}
"""
Nyckel = un,duex, trois dvs string
Värden = 1, 2, 3 dvs int
 """
#frns['un']    # element acces: 1
#frns['zero']  # KeyError: 'zero'
#frns['zero'] = 1  # add new entry "värde par" values can be duplicates dvs både un och zero har värdet 1, som kan finnas flera gånger
#frns['zero'] = 0  # update entry: keys must be unique, inget nytt värdepar utan bara nytt värde
# 'un' in frns      # membership  True
#3 in frns         # membership False-looking for keys, letar bland nyckel och inte bland värden
#del frns['zero']  # remove entry
#del frns['cinq']  # KeyError: 'cinq'

" iterate over KEYS in Dictionaries "
es = dict(uno=1, två=2, tre=3, fyra=4)  # nyckelord kommer tolkas som strängar och heltal är våra values

for key in es:
    print(f'{key} - {es[key]} ', end=',')  # access to the values
# output : uno - 1, två - 2, tre - 3, fyra - 4, sorterad ordning , använda key för att komma åt värden

" iterate over VALUE in Dictionaries"
for value in es.values():
    print(f'{value}', end=', ')  # no access to the keys
    # output: 1, 2, 3, 4,

" iterate over key-value pairs in Dictionaries"
for key, value in es.items():  # key, value kallas för tuple unpacking
    print(f'{key} - {value}', end=', ')
# output: uno - 1, två - 2, tre - 3, fyra - 4,
