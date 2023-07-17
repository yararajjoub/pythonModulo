""" Syntax error:"""  # Syntax- är regler och grammatik för hur man borde skriva Python-språket ex missat en punkt,
# avslutande parentheses eller indentering eller stavat fel eller fel reserverade ord, De hittas av utvecklingsmiljö
# -- inga output - vi får error innan vi körs koden
# EX på syntax-fel :
# for i in range(10)
#   print (i)
#   -- FEL --- "vi missade en kolon vid range(10)"

""" Runtime error"""  # Exekverings fel, händer när vi har ett korrekt syntax men är omöjligt att exekvera
# EX på Runtime-fel:
# Stavfel, felnamn på variable eller använt stora/små bokstäver i omvändsätt -- Vi får nameError
# String istället för int -- vi får då TypeError
# eller att vi försöker dela med zero (0)- ZeroDivisionError
# EXEMPEL:
# x = 5 + 7 / (5-5)  # är ett fel # division by zero

lst = [0, 1, 2, 3, 4, 5]
n = len(lst)
sista_elem_i_Lst = lst[n - 1]  # indexering börjar med 0, så sista elem är inte samma antal som listan,
# utan det är minus [n-1]
# Vi får- IndexError: list index out of range

number = input('n: ')
number += 1
# Type-error eftersom vi har input som String men vi bearbetar input som int

# import math
# diagonal = sqrt(2)  # missing the prefix: math.sqrt(2)

# det kan också vara att user matade in fel-data

""" Logic error """


# programmet körs, men ger fel resultat pga logisk fel i programmet eller kallas för semantisk fel
# man ska köra ett testfall för att kontrollera rätt resultat
# EX på logisk fel:
def if_sorted(listan):
    for i in range(len(listan) - 1):
        if listan[i] >= listan[i + 1]:
            return False
    return True


listaaa = [23, 434, 43, 22, 5, 4, 7, 8]
res = if_sorted(listaaa)
# equal values are considered unsorted
res_icke_sant = [1, 2, 2, 3, 5]  # vi får output: false - Not Expected
print(res)
# Det bero på att vi kontrollerar värdet på pos i är större än eller lika med pos i+1
# om 2 är lika med 2 kmr returneras false.
# Därför ska vi använda större än istället för lika med


""" Generating Exceptions genom att ange Assert- statement """
# assert condition, 'plain text error message'
# anger tydligt fel-meddelande och ger bättre felsökning.
" Ex på en function som kontrollerar validate av ett person-nr"
# sedan vi kallar denna funktion vid ett annat funktion som har giltigt-personnr som ett vikitgt steg innan den kan
# exekveras dvs (condition)
" efter assert vi skriver vår kondition o sen kan vi throw an exception "


def is_valid(id_number):
    pass


def open_bank_Account(id_number):
    assert is_valid(id_number), 'Invalid person number'


" Raise ExceptionType('plain text error message') # throw an exception istället för förra sättet, vilket är bättre"


# ex:
# python har inget /(bry sig inte om) typ av funktioners argument, tex list
# vi använder därför tex en raise statement för att bifoga en viss typ

def my_list_func(lst):
    if not isinstance(lst, list):
        raise TypeError('Expected a list')


# om vi kör den funktionen tex med en tuple kommer vi att få en: TypeError('Expected a list'), som vi raised tidigare
tuplee = (1, 2, 3)
my_list_func(tuplee)  # output: TypeError: Expected a list
