orden = input('Ange en serie ord, åtskilda av mellanslag: ')
data_list = orden.split(' ')
vokaler = 'aouåeiyäö'

# Konvertera till små bokstäver
data_list = [word.lower() for word in data_list]

# Välj ord som börjar med vokaler
firstLetter = [x for x in data_list if x[0] in vokaler or x[:2].lower() == "en"]

# Slå samman orden till en sträng med mellanslag som separator
result = ' '.join(firstLetter)

print(result)
