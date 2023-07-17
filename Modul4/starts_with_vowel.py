# Vi ska använda List Comprehension.
orden = input('Ange en serie ord, åtskilda av mellanslag: ')
data_list = orden.split(' ')
vokaler = 'aouåeiyäö'
# programmet ska hantera både små och stora bokstäver (upper/lower):
firstWord = [x for x in data_list if x.lower()[0] in vokaler]

# Slå samman orden till en sträng med mellanslag som separator
result = ' '.join(firstWord)
print(result)
