n = int(input('Enter a integer:'))

is_positive = n > 0 # True or False, alltså en boolean
if is_positive: # om is_positive är True
    print('I am positive!')
else:
    print('I am negative!')

is_odd = n % 2 # om resultatet är 1 = True, 0 = False
if is_odd:
    print('I am odd!')