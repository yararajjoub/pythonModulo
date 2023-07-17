# Läs in antal skor från användaren
nbr_left_shoe = int(input('Hur många vänsterskor finns det? '))
nbr_right_shoe = int(input('Hur många högerskor finns det? '))

# Räkna antalet hela par (höger och vänster), Genom att se vilken antal skor är minst
nbr_pairs = min(nbr_right_shoe, nbr_left_shoe)
# Beräkna antalet överblivna skor// abs = absoluta värdet, för att få negativ värde
nbr_left_over = abs(nbr_right_shoe - nbr_left_shoe)

# Anger om de överblivna skorna är högerskor eller vänsterskor
if nbr_right_shoe > nbr_left_shoe:
    shoe_type = 'högerskor'
else:
    shoe_type = 'vänsterskor'

# Anpassar texten om det blev över skor och vilken typ || om inga skor blivit över
if nbr_left_shoe == nbr_right_shoe:
    print(f"Det finns {nbr_pairs} par och inga överblivna skor.")
elif nbr_left_over == 1:
    print(f"Det finns {nbr_pairs} par och 1 överbliven {shoe_type}.")
else:
    print(f"Det finns {nbr_pairs} par och {nbr_left_over} överblivna {shoe_type}.")
