#Kysytään tunnit ja tuntipalkka
print("Syötä viikon työtunnit: ")
tunnit = float(input())
print("Syötä tuntipalkkasi: ")
tuntipalkka = float(input())

#Lasketaan normaalitunnit ja ylimenevät tunnit
if tunnit <= 40:
    normaalitunnit = tunnit
    yli_tyo_tunnit = 0
else:
    normaalitunnit = 40
    yli_tyo_tunnit = tunnit - 40

# Lasketaan palkka normaalitunneista ja ylitunneista erikseen
tuntipalkka = normaalitunnit * tuntipalkka
ylityopalkka = yli_tyo_tunnit * (tuntipalkka * 1.5)

# Lasketaan palkka
palkka = tuntipalkka + ylityopalkka

# Tulostetaan palkka kahteen desimaaliin pyöristettynä
print("Viikon ansiosi ovat: ", "{:.1f}".format(palkka)+ "€")