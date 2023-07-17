
n_kakor = int(input('Antal kakor: '))
n_barn = int(input('Antal barn: '))

# antal kakor som barn ska få:
kakor_Per_Barn = n_kakor // n_barn
antal_rest = n_kakor % n_barn

if antal_rest== 0:
    print(f'Det blir {kakor_Per_Barn} kakor per barn.')
elif antal_rest == 1:
    print(f'{kakor_Per_Barn} och Det blev en kaka kvar')
else:
    antal_rest > 1
    print(f'Det blir {kakor_Per_Barn} kakor per barn, och {antal_rest} över.')
