
def set_min_value(talLista, minValue):
    for i in range(len(talLista)):
        if talLista[i] < minValue:
            talLista[i] = minValue


lst = [4, -2, 0, 3, 7]
set_min_value(lst, 2)
print(lst)  # output: [4, 2, 2, 3, 7]
