lista = [456, 218, 101, 212]  # square brackets
Entuple = (111, 249, 244, 234)  # parentheses
emptyList = []
nothingInsideTuple = ()
# för att skapa endast EN element (1)
oneElmList = ['en']
oneElmTuple = ('alone',)  # viktigt med en komma tecken
# skapar en int:
oneInt = (1)
##man kan också ta bort paranteser, det är accepterat för läsbarhet
tuple1 = (2.323, 3.343)
tuple2 = 4.54, 3434.5, 3
tuple3 = 13,  # På det sättet skiljer vi mellan tuple och vanlig variable
# Listor och tupler kan innehålla olika datatyper samtidigt,
veggie = ['kalle', 3.4]  # etc
fruit = {'apple', 23.4}  # etc

s = 'hello'
listan = list(s)  # tilldela värdet från s
listaTillTuple = tuple(listan)  # tilldela värdet från listan
### ETT ANNAT SÄTT // ELLER : ###
first = list(range(5))  # [0,1,2,3,4]
center = tuple(range(-4, 5, 2))  # {-4, -2, 0, 2, 4} // 1.start, 2.stop, 3.steg (positive steg)

"""
på samma sätt för tomma lister och tuplar -- nada = list() --- voidsss = tuple()
 """

"""Index & Slicing """

enLst = [0, 2, 4, 6, 8]
tpl = (1, 3, 5, 7, 9)

# lst[2] Element Access - en viss index
# tpl[2] Element Access - en viss index

# Slicing operator

enLst[2:]  # start element 2 (0,1,2) och sluta vid sista elm
enLst[1::2]  # Start från 1, till slut, två steg i mellan, börja med att hoppa 2 steg

tpl[:2]  # Start från början, avsluta vid 2, utan den tredje -- (1,3) index(0),index(1)
tpl[3::-1]  # börja med index 3, till slut och gå ett steg bakåt

## iterera över elementen i listan
# exempel
lst = [42, 64, 36, 11, 70, 75]
for item in lst:
    if item % 2 == 0:
        print(item, end=' ')
# Output : 42 64 36 70

""" Ett annat sätt, att använda range obj """
tpl = (8, -4, 10, 3, -7, -2)
counter = 0
for i in range(len(tpl)):
    if tpl[i] > 0:  # om siffra är positiv tal
        counter += tpl[i]
print(counter)
# (0 + 8 + 10 + 3 = 21), 5gånger, iterera över index vi har


########
# Enumerate, vi får både index och element,
fruits = ['apple', 'banana', 'cherry', 'orange']
for index, item in enumerate(fruits):
    print(index, item)
    # output
    # 0 apple
    # 1 banana
    # 2 cherry
    # 3 orange
for i in range(len(fruits)):
    print(i, fruits[i])

### unpacking, allt detta går under unpacking ###
# packa in och ut
# Där vi skapar en tuple/list utifrån en/flera variabler , ex:
animals = ('mio', 'natacha')
dog, cat = animals  # dog = mio, cat = natacha
### detta ingår / motsvara enumerate()
# for index, item in range(fruits):     print(index, item)
# enumerate() packs , the index and elements into a tuple
# index, item unpacks the tuple into the variables index and item
# Use tuple unpacking för att switcha mellan två värden, ex
a = 0
b = 1
a, b = b, a  # switcher mellan värden i a och b dvs b blir 0, och a blir 1
# behöver ej ha temporär variable

# Lit Comprehension -- som skapa en ny lista från en befintlig lista, det går inte att göra en Tuple Comprehension
lst = [-4, 0, 3, 6, -5]
absoultValue = [abs(x) for x in lst]  # 4, 0, 3, 6,-5
## ELLER ##
squres = [x * x for x in range(5)] # [0, 1, 4, 9, 16]

# List comprehensions can include a condition
readings = [12, 9, 13, 10, 6]
valid = [x for x in readings if x >= 10]
print(valid)
# OutPut: 12, 13, 10

# funktioner som är till tupler och lister (sekvenser)
len(lst)  # the length of sekvensen, nbr of elemn
min(lst)  # minimum element
max(lst)  # maximum element
sum(lst)  # sum of element / bara om det går att räkna, INTE för String eller txt, beroende på datatypen


userData = input('Sale prices: ')
data_list = userData.split(' ')  # gör en string till en lista, delar upp strängen userData vid mellanslagen
# och skapar en lista 'data_list'
prices = [float(x) for x in data_list]  # list comprehension

n = len(prices)  # antal elem i prices listan
avg = sum(prices) / n  # average är summan av antal elem listan delat på antal dem
print(f'{n} products, average price: {avg:.2f}')

