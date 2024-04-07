#otsikko ja taulukko muuttujat
otsikko = ["Etunimi", "Syntymävuosi", "Palkka", "Veroprosentti"]

taulukko = [
    ["Matti", 1970, 2000, 22.8],
    ["Maija", 1980, 2500, 27.7],
    ["Paavo", 1990, 1000, 19.7]
]

#Printataan eka otsikko ja sitten rivit
print("{:<15} {:<15} {:<10} {:<15}".format(* otsikko))

for row in taulukko:
    print("{:<15} {:<15} {:<10} {:<15}".format(*row))
