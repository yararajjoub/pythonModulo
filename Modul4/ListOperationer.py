# Listor är muterbara, men inte Tupler
# Det betyder att object som är mutable-datatype kan ändras (ändra sitt värde) efter att skapa den.
# Vi kan inte ändra, lägga till eller ta bort nått från en tuple, eftersom den är icke-mutable.
"""
#ändra värde i en lista:
lista = [1, 2, 3, 4, 5]
for item in lista:
    item = item * 2
print(lista)   # Output: [1, 2, 3, 4, 5]
Här ändrar vi inte listan, utan vi ändrar värdet bara på item, vilket inte tillhör listan
"""
# Attempt 2, vi kan ändra värde i en lista eftersom den är muterbar
lista = [1, 2, 3, 4, 5]
for item in range(len(lista)):
    lista[item] = lista[item] * 2
print(lista)  # Output: [2, 4, 6, 8, 10]
"""
for item in list:
innehålla endast en kopiera av elementen, den är bästa sättet om vi vill endast iterera över
 elementen utan att ändra nått i listan. 
 for item in range(len(list)): // är den metoden som vi använder för att ändra i listan
 ändrar själva elementen inuti listan 
 """

# Operationer som används till Listor:
lista2 = []
i = 0
j=2
k= 0
lista.append(item)  # Lägger till elementen 'Item' i slutet av listan.
lista.extend(lista2)  # Adds lista2 to the end of the list lista
lista.insert(i, item)  # Inserts the element 'item' at the position 'i'
lista.clear()  # Removes all the elements in the list
lista.pop()  # Removes and returns the last element of the list
lista.pop(i)  # Removes and returns the element at the position 'i'
lista.remove(item)  # Removes the first occurrence (den första förekomma item, om flera skulle finnas så tas bort endast
# den första, of the element 'item'
########
#Exempel:
lista = [1, 2, 3, 4, 3, 5, 3]
item = 3
lista.remove(item)
print(lista)  # Output: [1, 2, 4, 3, 5, 3]
########
lista.copy()  # Kopierar & returnerar listan
lista.remove()  # Reverses the order of the list
lista.sort()  # Sorterar elementen i listan
del lista[i]  # tar bor element vid index 'i' från lista, det påverkar listan direkt genom att ta bort elementet på
# Plats. Det gör att listan fixar ordning på elementen igen för att fylla på gapet och minska storleken.

"""jämfört med remove(item), vi tar bort första förekomsten av ett element med värdet 'item'
 Så sammanfattningsvis, del list[i] tar bort ett element baserat på dess index i listan,
medan lista.remove(item) tar bort det första förekomsten av ett element baserat på dess värde.
"""

del lista[i: j: k]  # Removes the slice i:j:k // start-index, slut-index, steglöngd, kodition för att ta bort elem
# Exempel
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del lista[1:7:2]  # starta index 1, slut index 7, hoppa av 2 steg
print(lista)  # Output: [1, 3, 5, 7, 8, 9]


# Fibonacci = varje tal i serien är summan av två förgående talen.
""" det början med talen 0 och 1, så fortsätt genom att addera de två senaste talen för att få nästa tal
0,1,1,2,3,5,8 etc """
f = [0, 1]  # vår talserie börjar med 0,1
for i in range(5):  # iterera 0,1,2,3,4 (5 gånger)
    f.append(f[-1] + f[-2])  # F-1 betyder den sista index i listan, f-2 näst sista i listan. Vi lägger till sum av dem
print(f)

listaTaBort = [1, 2, 3, 4, 5, 6]
nTal = listaTaBort.pop()  # Sista elem i listan
mTalet = listaTaBort.pop(2)  # Ta bort elem från position '2' i listan
del listaTaBort[1:3]  # Börja med index 1 sluta med 3, ta bort 2 ny lista blir:
# 1,2,3,4,5 (nTal)
# 1,2,4,5  (mTal)
# (ind-1 slut 3-).. Elementen med ind 1 och 2 kommer att tas bort ind1 = [2], ind2 = [4]
# output = [1,5]
