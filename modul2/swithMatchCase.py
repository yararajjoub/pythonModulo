# Switch case in Python
"""
n = int(input('Number of children:'))
allowance = 1250 * n
match n: # match case /(switch case) in Java
    case 1:
        pass # pass betyder att vi inte gör något/
        # eftersom vi redan har räknat ut N som betyder ett barn
    case 2:
        allowance = allowance + 150
    case 3:
        allowance = allowance + 730
    case 4:
        allowance = allowance + 1740
    case 5:
        allowance = allowance + 2990
    case _: # default case
        allowance = allowance + 4300
print(f'Total Allowance: {allowance}')
"""
name = input('Enter your name:')
match name:
    case 'Kalle':
        print('Hej Kalle')
    case 'Lisa':
        print('Hej Lisa')
    case _: # default case
        print('Hej okända personen: ', name)
# match case kan användas för att jämföra med flera olika värden

