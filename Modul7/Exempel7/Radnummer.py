# Läsa innehållet från en textfil och skriv ut det till console. Raderna ska också vara numrerade

filename = input('Enter File Name: ')
with open(filename, encoding='utf-8') as filen:
    content = filen.readlines()  # läsa innehållet i filen radvis
# skriva ut innehållet med radnummer
#print(content)  # ligger i en lista, varje elem är en Sträng och \n som innebär ny rad
"""
for line in content:
    print(line[:-1])  # utan sista tecken
"""
""" 
for index in range(len(content)):
    line = content[index] # line = content[item] denna raden finns redan i enumerate, så vi behöver inte den längre
    print(index, line[:-1])
"""
# Ett annat sätt än det kan vi använda enumerate:
for i, line in enumerate(content): # unpacking
    print(i, line[:-1])
