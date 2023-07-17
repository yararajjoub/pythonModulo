#Modulo 2 första lektionen


#print(f'Du har tagit {belopp}, Du har kvar {saldo}')
#denna verisonen gör att vi får NEGATIVT värdet, dvs mer ön det vi har i saldot,
#vilket är fel och måste göras om, anpassa programmet med user-matning

#använd IF-sats, Indentation= att lämna mellanrum under IF-satsen, vilket betyder
#att de är under samma block och ska utföras samtidigt- annars får syntax erorr
"""
saldo = 100
belopp = int(input('välj belopp:'))

if belopp < 0:
    print('Du kan inte ta ut negativt belopp')

elif saldo >= belopp:
    saldo = saldo - belopp
    print(f'Ny Saldo: {saldo}')

else:
    print(f'Du har inte tillräckligt med pengar, Ditt Saldo är:{saldo}')

Python-translatorn förstår att slutet på ett kodblock nåtts, genom att:
Ett kodblock avslutas då nästa rad är mindre indenterad
Python använder indentering för att identifiera kodblock.

"""
#ett annat exempel med IF-sats
number = int(input('Enter a positiv integer:'))
if number >= 0:
    if number % 2 == 0: # % betyder att vi ska kolla om det är jämnt eller inte
        print('Number is even')
    else:
        print('Number is odd')
else:
    print('Number is negative')