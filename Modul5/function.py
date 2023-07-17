def minstaTal(a, b):
    if a < b:
        return a + b
    else:
        return b + a
x = 2
y = 3
m, M = minstaTal(x, y)
print(f'x = {x}, and y = {y}')
print(f'The minimum value is {m}')
print(f'The maximum value is {M}')
#############

def greet(name):
    print("Hello, " + name + ". Good morning!")

user_name = input("Whats your name: ")
greet(user_name)


#############

def avg(a, b):
    return (a + b) / 2


first = int(input('Enter first number'))
second = int(input('Enter second number'))
result = avg(first, second)
print(result)


############


def swapp(a, b):
    a, b = b, a
    return a, b


x = 2
y = 3
x, y = swapp(x, y)
print(f'x = {x}, and y = {y}')


############

def minmumNumber(a, b):
    if a < b:
        return a
    else:
        return b


a = int(input('Enter first number'))
b = int(input('Enter second number'))
result2 = minmumNumber(a, b)
print(f'{result2} is the smallest number')

## man kan också använda return som break istället för att skriva else om det var sant, exempel:
def minmumNumber(a, b):
    if a < b:
        return a
    return b
