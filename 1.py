def bosan(daftar):
    for x, y in enumerate(daftar):
        try:
            print(y[-1-x], end='')
        except:
            print('x', end='')
        
daftar = ("Yusta", "Monic", "Claresta", "Elisabeth", 
"Agustin", "Anastasya", "Wijaya")
bosan(daftar)