print('back' < 'Hack')
print('back'.lower() < 'HAck'.lower())
# We compare if it's the same length and same elements
""" A < B, < C < ..... < Z < a < b < c < ..... < z """
print('abc' == 'abc')
print('defogger' == 'srf')
print('abc' < 'abd')  # True --- a < b < c < d

s = 'connexion'
print(f'There is an x in {s}: {"x" in s}')

mittNamn = 'Yara Rajjoub'
print(f'det finns z i mitt namn: {mittNamn}, svaret: {"z" in mittNamn}')

print('old' in ' f old ed')  # sub sequences, output: true

str = 'yararajjoub'  # 11 carch, index from 0-10
print(f'[{str} börjar med {str[0]} och slutar med {str[10]}')
print(f'the last char in the string: {str[-1]} & the second last one is: {str[-2]}')

ste = 'FBI'
for i in range(len(ste)):
    print(ste[i], end='-')
print()
for j in range(len(str)):
    print(str[j], end='.')
print()

for i in range(len(ste)):
    print(ste[-i - 1], end=' ')  # output:  I B F
print()

for i in range(len(ste)):
    print(ste[i])
print()

bokstavString = 'Hello Some Sensitive subject in the school'
for charactar in bokstavString:
    if charactar in 'aeiouy':
        print('*', end=' ')
    else:
        print(charactar, end=' ')
# Output blir: H * l l *   S * m *   S * n s * t * v *   s * b j * c t   * n   t h *   s c h * * l


### Vi kan inte ändra en datatyp efter att skapat den- Immutable ###
"""Exempelvis kan vi inte ändra: int, float, str, bool """
#Skillnaden blir därför :
"""
List - mutable, det går att modifiera 
Tuple- immutable 
"""
