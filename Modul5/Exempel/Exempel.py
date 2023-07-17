# Variationsberedd
# Skriv en funktion som tar en lista och returnerar dess variationsbredd. Skriv även kod som
# anropar funktionen. (Inom statistik är variationsbredden ett mått på skillnaden mellan det största och det minsta
# värdet i en samling mätvärden.)

def functionen(lst):
    skillanden = max(lst) - min(lst)
    return skillanden


minList = [5,1,0,-2,9,-3,12]
#mattet = functionen(minList)
print(functionen(minList))