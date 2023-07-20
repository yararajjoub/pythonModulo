#hantera flera ord och hantera även stora bokstäver
from Modul5.Exempel import sprak

#sprak.translate(original) återanvänt funktion från en module och lagrade data i filen

with open('random.txt', encoding='utf-8') as f:
    fulltext = f.read()  # en sträng

translation = sprak.translate(fulltext)

with open('rovarsprak.txt','w', encoding='utf-8') as f:
    f.write(translation)

    """
    processen går såhär:
        läsa-- modifiera -- skriva
    """