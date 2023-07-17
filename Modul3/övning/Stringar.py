långt_ord = 'högskoleingenjörsutbildning'
for i in range(len(långt_ord)):  # hur många bokstäver har långt_ord?
    # skriv ut bokstaven på position i i långt_ord, avsluta med punkt
    print(långt_ord[i], end='.')
print()

"""
ord = input('Skriv ett ord som innehåller bokstaven x: ')
# om bokstaven x inte finns i ordet
x='x'
if x not in ord:
    print('Det finns inga x i ordet')
else:
    print('det finns ett x i ordet:',ord)
# skriv ut felmeddelande



# Fråga, vara och svar
quest = 'vad vill du ha? '

vara = input(quest)
svar = f'denna {vara} finns inte längre'
print(svar)

######
ord = input('Skriv ett ord: ')
första = ord[0]        # strängens första tecken
fjärde = ord[3]         # strängens fjärde tecken
sista = ord[-1]          # strängens sista tecken: kom ihåg att vi inte vet hur lång strängen är!
baklänges = ord[::-1]      # använd slicing för att vända på strängen

print(f'Ordet börjar på {första} och slutar på {sista}.')
print(f'Ordets fjärde bokstav är {fjärde}.')
print(f'Baklänges blir det {baklänges}.') """
