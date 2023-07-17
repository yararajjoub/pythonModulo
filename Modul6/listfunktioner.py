def arg_min(lista):
    if len(lista) == 0:
        raise ValueError('Det är en tom lista')
    min_pos = 0
    min_value = lista[0]
    for index in range(len(lista)):
        if lista[index] < min_value:
            min_pos = index
            min_value = lista[index]
    return min_pos
""" 
values = [6, 3, 4, 8, 1, 5]
min_pos = arg_min(values)
print(min_pos)  # Output: 4

values = [14, 24, 10, 15, 10]
min_pos = arg_min(values)
print(min_pos)  # Output: 2

values = []
try:
    min_pos = arg_min(values)
    print(min_pos)
except ValueError as e:
    print(e)  # Output: Fel: Tom lista
"""


# Hitta positionen en lista med positionerna:
def find_all_positions(values, tal):
    nyLista = []
    for index in range(len(values)):
        if values[index] == tal:
            nyLista.append(index)
    return nyLista

""" 
values = [3, 3, 5, 2, 6, 5, 4, 5, 3, 2]
min_pos = find_all_positions(values, 3)  # [0, 1, 8]
print(min_pos)
"""