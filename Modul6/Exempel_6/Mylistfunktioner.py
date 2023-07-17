# Skapa en funktion som returnerar positionen för listans största element.
# Skapa en modul som innehåller funktionen.
"""
def listsElemIndex(listan):
    #max_val = listan[0]
    max_val = 0 # Det är en gissning på att det är minst, men jag kan skriva annat ex första [i] i listan
    #itererar över elementen i listan
    for index in listan:
        if index > max_val:
            max_val = index
    return max_val
    # print(max_val)


minList = [23, 1, 2, 3, 4, 33]
result =listsElemIndex(minList)
print(result)

"""
""" 

def arg_max(lst):
    max_pos = 0
    #iterera över positionerna i listan
    for index in range(len(lst)):
        if lst[index] > lst[max_pos]:
            max_pos = index
    return max_pos
#körs bara om denna är mainet-modulenamn-
if __name__ == '__main__':
    minList = [23, 1, 2, 3, 4, -33]
    result =arg_max(minList)
    print(result)
"""



# låta user försöka ända fram till de får en giltigt input, ex tal då gör vi följande:

#try:
def arg_min(lista):
    if lista == []:
        raise ValueError('tom lista')
    min_pos = 0
    for index in range(len(lista)):
        if lista[index] < lista[min_pos]:
            min_pos = index
        return min_pos


if __name__ == '__main__':
    try:
        values = []
        min_Position = arg_min(values)
        print(min_Position)
    except ValueError as e:
        print(e)  # Output: Empty list



""" 
def arg_min(lista):
    if not lista:
        raise ValueError('tom lista')
    min_pos = 0
    for index in range(len(lista)):
        if lista[index] < lista[min_pos]:
            min_pos = index
        return min_pos


if __name__ == '__main__':
    try:
        values = [2, 3, 4, -56, 666, 64,4]
        min_Position = arg_min(values)
        print(min_Position)
    except ValueError as e:
        print(e)  # Output: Empty list

"""
