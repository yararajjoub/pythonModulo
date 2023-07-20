# ett program som läser in varor från användaren och skriver ut totala priset
# priser för de olika varorna ska lagras i en dictionary
"""  Nycklar är varor och värden är priser """

prislista = {'äpple': 10, 'päron': 12, 'banan': 8, 'kiwi': 30}
total = 0
try:
    while True:
        user_data = input('Enter varorna, q för att avsluta:')
        if user_data == '':
            break
        total += prislista[user_data]  # prislista[user_data] är värdet till nyckeln user_data
    print(f'Det blir {total} kr.')
except KeyError:
    print('Varan finns inte i prislistan.')
