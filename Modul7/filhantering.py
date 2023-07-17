# lagra data för permanent och utbyta data
# oformaterad text, (ingen info om strk, färg och texttypssnitt)

# streaming / strömmar:
# standard output - när vi skriver ut texten till skärmen "stdout"
# standard input - läser in input från user "stdin"
# standard error - där fel meddelanden hamnar "stderr"
# Vi ska fokusera på att läsa och skriva från filer


" Att skapa o skriva i en fil "

# Öppna
filnamn = "fruits.txt"
fil = open(filnamn, "w")
# Att skriva in data
fil.write("banan, \ncherry, \näpple, \ncitron\n")
fil.write("\nBy: Yara")
fil.close()

" Att läsa från en fil "
# vi måste ha den eller skriva den
filen = open('fruits.txt')  # här öppnar vi filen, returnerar en referens till file-obj
for row in filen:  # här READ läser vi line by line
    print(row, end='')  # print the line
filen.close()  # close

# if the opening-operation fails, an OSError will be raised
" The built-in function open()"
" Den tar emot tre parametrar (av datatypen sting) "
" filen = open(filnamn, mode (dvs skriva eller läsa), encoding = enc) UTF-8"

"""

 mode =   r - read file must exit, default 
          w - write, creates a new file, or overwrites befintlig fil
          x - write, creates a new file, file cannot exist (fel-medd) om den inte finns
          a - write, appends if the file already exists/ lägger till i slutet att filen redan finns
          r+, w+ - read and write

"""

" With - statement "

# with open(filen) as f:
    # code block

# detta läser från filen, denna statement catshar inte errors
# används om filen öppnas så stängs den sedan garanterar att filen är stängd, vi behöver inte använda filen.close,
# oavsett om det gick fel eller gick bra
with open('fruits.txt') as myFile:
    word_count = 0
    for row in myFile:
        line_lst = row.strip().split()  # 2 funktioner sker efter varandra
        word_count += len(line_lst)
    print('Number of words: ', word_count)  # output:Number of words:  6


# line_lst = row.strip().split()  # strip: Detta är användbart för att rensa bort onödiga mellanslag eller
# tabbar som kan finnas i början eller slutet av strängen. # Split() dela upp strängen

# skriva till en fil, från user_input
with open('groceries.txt', 'a') as f:  # Append if file existing
    print('Add to shopping list: ')
    while True:
        item = input('vad vill du lägga till? ')
        if item == '':
            break
        f.write(item + '\n')  # write to the file

# det kommer att printas till och med alla lagrade data
shopping_List_fil = open('groceries.txt')  # här öppnar vi filen, returnerar en referens till file-obj
for row in shopping_List_fil:  # här READ läser vi line by line
    print(row, end='')  # print the line
shopping_List_fil.close()  # close


" funktion: att läsa från filen som användare ber om, med felhantering"
# Hantera fel som uppstår :
while True:
    try:
        fil_namn = input('Enter file name: ')
        with open(fil_namn, 'r') as f:  # file must exist, stängs efter körning oavsett fel eller ej
            for row in f:
                pass  # do the work here, do something
        break  # upprepa tills filen öppnades, ta ut oss ur while-satsen
    except FileNotFoundError:
        print('File not found:', fil_namn) # skickar inte felet vidare