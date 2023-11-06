#Agus Setiawan
#312310597
#TI.23.A6

baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab),end='')
    print()