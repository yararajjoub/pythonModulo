import math
import datetime
# Literal är en konstant värde i koden
s = 'This is String'
s2 = "This is also another String"
# man kan placera text på flera olika rader redan här
s3 = '''This is 
a triple
String'''

sEmpty = ' '



# problem = 'this won't work'
solution = "This os how it´s done"
orThatWay = ' "like that" AS CITAT'


##( \ ) backslash måste stå själv och inget annat skrivs efter den, och börja med nytt rad efter
string = 'testa, ' "att" \
         ' Köra något nytt '
print(s3)

print(f'formatted string, want to print the value of pi : {math.pi:.4f}')
print(r'c:\user\right what do you want without having backslash to annoy you')

ss = 'this' ' and '
ss2 = 'that'
print(ss + ss2)  # output blir: this and that

# Repeat the String
repString = 'Hej ' + 'Y' + 'a' * 2 + 'r' + 'a' * 3 + '!'
print(repString)  # Output blir: Hej Yaaraaa!

stringen = "Iam Yara"

stringen.isdecimal()  # Returns TRUE/False if all characters are decimal numbers
stringen.isalpha()  # Returns TRUE/False if all characters are alfapet
stringen.isupper()  # Returns TRUE/False if all characters ar uppercase (Stora bokstäver)

stringen.lower()  # Returns copy of all characters in lowercase (ändrar karaktärer till små bokstäver)
stringen.upper()  # Returns copy of all characters in Uppercase (ändrar karaktärer till stora bokstäver)
stringen.replace('old Str', 'new Str')  # Returns copy of all characters replacing old "str1" to new "str2"

print(stringen.upper())  # Output: IAM YARA
print(stringen.replace('Y', 'S'))  # OutPut: Iam Sara
#stringen[2] = 'W' -- Error
#print(stringen) -- Error
# Vi kan inte tilldela Stringen ett nytt värde.
print(stringen.isdecimal())  # OutPut: False


datetimeString = datetime.datetime.now()
print(datetimeString)  # Output kommer att vara: 2023-06-20 13:48:54.283764
""" Attributes: 
Datum: år, månad, dag, Tid: timme, minut, sekund, mikroSek? """
print(f'Formatted string datum & tid är {datetimeString.month}/{datetimeString.day}/{datetimeString.year}')
#Outputen blir så istället: Formatted string datum & tid är 6/20/2023

