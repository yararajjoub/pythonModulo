def fun(a, b, c):
    print(a, b, c)


x = 1
y = 2
z = 3
fun(y, c=x, b=z)  # Keyword argument


# c har fått värdet till X vilket är 1, men C kommer i index 3 i funktionen sista

#######
# default värde för parameter, de kommer sista
def funcc(a, b, c=0):
    print(a, b, c)


x, y, z = 1, 2, 3
funcc(z, b=y)  # default argument behöver ej intitierar här


# output: 3,2,0

######
def f(a, b=0, c=0):
    print(a, b, c)


x, y, z = 1, 2, 3
f(z, c=y)  # 3,0,2 # 1:a positional, 2:a default, 3:e keyword
""" ANY arguemnts given after a default value has been used must be named, dvs Keyword (b=x)"""

""" 
A variable numver of arguments
arbitrary arguments
Python Arbitrary Arguments allows a function to accept any number of positional arguments
i.e. arguments that are non-keyword arguments, variable-length argument list

om vi inte vet hur många antal parameterar användare kommer att lägga till
ex:
ange telnr *
ange postnr *
ange ort (default/ optional)
ange gmail (default/ optional)
ange namn (default/ optional)
ange personNr * 
"""


def printLast(*people):  # blir en tuple
    print(f'Last, but not least: {people[-1]}')  # skriver ut som om det vore en tuple


printLast('Jack', 'Jill')  # här kan man ange hur många argument som helst, inga gränser


#########
# variablet antal argument, delar upp argument i två kategorier och adderar de separata och returnerar de separata
def sum_separately(*values):
    positive, negative = 0, 0
    for item in values:
        if item < 0:
            negative = negative + item
        else:
            positive = positive + item
    return positive, negative


revenue, expenses = sum_separately(2, 3, -2, -7, 0, 1)  # inkomst, utgifter

print(f'Revenue: {revenue}, Expenses: {-expenses}')  # output: Revenue: 6, Expenses: 9

# minus tecken framför expenses -- eftersom vi vill att negativa talet ska vara positiva tal (-9 blir 9)
""" Viktigt att tänka på:varje argument som kommer efter *arg måste vara named-value dvs limit = 0"""


def sum_sep(*valu, limit=0):
    pos, neg = 0, 0
    for item in valu:
        if item < limit:
            neg += item
        else:
            pos += item
    return pos, neg


big, small = sum_sep(2, 12, 13, 7, 19, limit=10)  # Vår limit. Python ska förstå att sista argument är inte value utan
# att det är limit
print(f'Small fish: {small}, Big fish {big}')

####
""" En del funktioner kallas för metoder,
Metoder är de funktioner som är associerade med object från specifik klass """
#Exempel:
# lst.pop(indx), listans namn punkt funktionens namn
# lst.append(item)
