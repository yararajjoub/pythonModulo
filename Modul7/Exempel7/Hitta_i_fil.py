# Läs innehållet från en textfil och skriv de rader som innehåller ett givet ord till en ny fil. Inkludera radnummer

filename = input('Enter file name: ')
givet_ord = input('Sökta ordet: ')
# Öppna filen
with open(filename, encoding='utf-8') as filen:
    content = filen.readlines() # en lista som innehåller alla rader

new_Content = []
for i, line in enumerate(content):
    if givet_ord in line:
       # print(i, line, end='')
        new_Content.append(str(i) + ': ' + line)

new_filename = filename[:-4] + '_' + givet_ord + '.txt'

with open(new_filename, 'w', encoding='utf-8') as new_file:
    new_file.writelines(new_Content)
