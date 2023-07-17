numSerie = input('Ange en serie heltal, åtskilda av mellanslag: ')
data_list = numSerie.split()
numTarget = int(input('Ange ett målvärde: '))
# En variabel för att hålla reda på det närmaste talet och initialisera den med det första talet i serien:
closest = int(data_list[0])
# Räkna avstånd mellan avståndet mellan det närmaste talet och målvärdet
distans_mellan_Tar_Serie = abs(closest - numTarget)
# Iterera över resten i Listan och uppdatera closest och distans om det finns ett närmare tal:
for i in data_list:
    aktuellaDistans = abs(int(i) - numTarget)
    if aktuellaDistans < distans_mellan_Tar_Serie:
        closest = int(i)  # uppdatera närmaste
        distans_mellan_Tar_Serie = aktuellaDistans
print('Närmast:', closest)
