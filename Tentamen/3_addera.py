# en funktion som tar en lista av heltal och returnerar summan av de positiva talen i listan.
def addera_positiva(lista):
    # lista = int(input('Ange heltal lista att addera: '))
    summa = 0
    for tal in lista:
        if tal > 0:
            summa += tal
    return summa


# Test indata
# [10, -1000, 10, -100000, 10, -10, 10] # output 40
# [4, 1, 0, -5, 4, -1, -8, 0] # output 9

lista_str = [-6, -3, -9, -12, -7, -2, -1]  # output 0
summan_tal = addera_positiva(lista_str)
print(summan_tal)
"""
summan_tal = addera_positiva([10, -1000, 10, -100000, 10, -10, 10])
print(summan_tal)
"""
