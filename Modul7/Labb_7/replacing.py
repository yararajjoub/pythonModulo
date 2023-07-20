"""
Skriv ett program som ersätter alla förekomster av ett givet ord i en fil med ett annat ord.
Programmet ska läsa in filnamn, ord att ersätta samt ord att använda istället från användaren via kommandoraden.
Notera att den ursprungliga filen ska skrivas över.
 Exempel på körning:

 Ange ett filnamn: kort_saga.txt
 Ord att byta ut: gång
 Ersätt med: VÄG

 Ledtråd: Använd sträng-funktionen replace.
 """
fileName = input('Ange ett filnamn: ')
oldWord = input('Ord att byta ut: ')
newWord = input('Ersätt med: ')

with open(fileName, encoding='utf-8') as file:
    fileContent = file.readlines()


replacedFileContent = []
for i, line in enumerate(fileContent):
    replacedFileContent.append(line.replace(oldWord, newWord))


with open(fileName, 'w', encoding='utf-8') as file:
    file.writelines(replacedFileContent)
