# Try - Statement ex, oväntad input, eller att öppna filer
# misstänker att det kan gå fel och får en exception, så kan vi hantera detta felet

try:
    user_Data = input('Enter a number: ')
    number = float(user_Data)
    print(f'Inverse: {1 / number}')
except Exception as e:
    print(e, 'hej från e')
except ValueError:
    print(f'Invalid number: {user_Data}')
except ZeroDivisionError:
    print(f'Zero has no inverse')
except(TypeError, NameError):
    print('Other type of error, it can be one of them')
else:
    print('Om inget gick fel så körs den om man tog sig ur try utan nått exception eller break'
          'Fel i else blocket så kan det inte hanteras av tidigare except, därför vi använder det inte så vanligt')
    raise 'pass along the exception'
finally:
    print('denna körs oavsett om det gick bra eller exception var thrown, ex vid stänga en fil')

# låta user försöka ända fram till de får en giltigt input, ex tal då gör vi följande:
while True:
    try:
        user_Data2 = input('Enter a valid number: ')
        number = float(user_Data2)
        print(f'The inverse: {1 / number}')
        break
    except ValueError:
        print(f'Invalid number: {user_Data2}')

# EAFP, stor risk att vi gör fel, felhantering ganska billigt mindre resurser
try:
    x = input('enter what u want ')
    number = float(x)
    y = 1 / number
    print(f'The inverse: {y}')
except:
    pass  # händer inga crash
