"""
i = 0
while i < 10:
    print(i, end=' ')  # end='' betyder att vi inte ska göra en ny rad
    i += 1
print()
"""
# Spara mål

goal = float(input('Savings gaol: '))  # mitt sparmålet

balance = 0  # det jag har nu i mitt konto
counter = 0  # för att räkna hur många gånger tog det för att komma fram till målet.
while balance < goal:  # fortsätt i loopet så länge jag har ej nått målet, dvs sparandet är mindre än målet
    amount = float(input('Deposit: '))  # mitt konto uppdateras varje gång jag lägger till nått nytt belopp,
    # tills cond = false
    if amount < 0:
        print('No withdrawals')
        # break
        continue  # betyder istället att avbryt BARA denna iterationen men inte hela loopen, ifall input var negativ 
        # av misstag
    balance += amount
    counter = counter + 1
else:  # bara om loopen inte avbröts med BREAK
    print(f'You have reached your goal: The balnce is: {balance}, under {counter} månader')




# En annan typ av While, cond är kontrollerad i början, men inte alltid kan göras så. Därför kan vi köra
# en iteration utan kolla cond utan kör tills vi bryter med BREAK
# vi vill fråga användare om en jämn tal
while True:
    even = int(input('Enter even number: '))
    if even % 2 == 0:
        break
    print(f'Not an even number')