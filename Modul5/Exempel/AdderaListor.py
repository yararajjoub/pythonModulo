#skriv en funktion som ar in två lika långa listor, adderar dem elementvis och returnerar en lista som innehåller resultatet.
#De två ursprungliga listorna ska inte ändras
def adderaListor(list1, list2):
    result = []
    for i in range(len(list1)):
        summa = list1[i] + list2[i]
        result.append(summa)
    return result

minlist1 = [1,2,3,4,5]
minlista2 = [6,7,8,9,10]

newList = adderaListor(minlist1,minlista2)
print(newList)