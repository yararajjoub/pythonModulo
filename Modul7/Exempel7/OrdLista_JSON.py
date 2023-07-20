# user skapar en sv-en ordlista, ordlistan ska lagras i en variable av typen dictionary
import json

with open('ordlista.json', encoding='utf-8') as file:
    ordlista = json.load(file)  # läsa in ordlista från filen

#ordlista = {}  # en dictionary

while True:
    svenska = input('Ange ett svenskt ord: ')
    if svenska == '':  # om tom sträng, gå ut ur while
        break
    engelska = input('Ange översättning på svenska: ')
    ordlista[svenska] = engelska  # lägga till ett par i dictionary, svenska är nyckel, engelska är värdet
# värden kan vara av vilken typ som helst men nyckeln måste vara text
#print(ordlista)
# för att lagra tidigare inmatade ordlistan kan vi lagra dem i en fil
# vi kan använda JSON format

with open('ordlista.json', 'w', encoding='utf-8') as file:
    json.dump(ordlista, file)  # dumpa ordlista i filen
