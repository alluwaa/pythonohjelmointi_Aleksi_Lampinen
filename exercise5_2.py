kuukausi = 1
sade_maara = 0
for x in range(12):
    print("Anna "+ str(kuukausi) +".kuukauden sademäärä: ")
    tulos = float(input())
    sade_maara += tulos
    kuukausi += 1
keskiarvo = sade_maara / 12
print ("Vuoden keskiarvo on n. {:.1f} mm".format(keskiarvo))
