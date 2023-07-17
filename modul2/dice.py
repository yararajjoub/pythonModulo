import random

# En seriekast
# Inga gissningar än, därför upprepa tills cond är true
antalKast = 0
while True:
    antalKast = antalKast + 1  # counter

    gissning = random.randint(1, 6)  # random tal mellan 1-6
    print(gissning)
    if gissning == 6:  # vår condition blev true
        break

print(f'Det tog {antalKast} kast att få en 6:a.')
