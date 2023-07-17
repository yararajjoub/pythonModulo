#Ange ett par tal: 12 15 5 4 10 4 12 5 15
#Ange ett sökt tal: 5
#Det minsta talet finns på position 3.
#Talet 5 finns på positionerna [2, 7].

import listfunktioner

user_Data = input('Ange ett par tal: ')
user_Tal = int(input('Ange ett sökt tal: '))
# vi får en ny lista genom Listkomprehensionen
user_Data = [int(x) for x in user_Data.split()]

my_min = listfunktioner.arg_min(user_Data)  # viktigt punkt
print(f'Det minsta talet finns på position {my_min}.')

find_nbr = listfunktioner.find_all_positions(user_Data, user_Tal)
print(f'Talet {user_Tal} finns på positionerna {find_nbr}.')