#Agus Setiawan
#312310597
#TI.23.A6

import random
print("=bilangan acak yang lebih dari 0,5 =")

jum = int( input("masukan nilai: "))
i = 0
while i in range(jum):
    i += 1
    angkarandom = random.uniform(0,0.5)
    print("bilangan ke:",i, ":", angkarandom)