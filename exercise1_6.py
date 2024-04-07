# Kysytään käyttäjältä senttimäärä + virheilmoitus jos ei ole väliltä 1-100
print("Anna 1-100 senttiä")
while True:
    kolikko = int(input())
    if 1 <= kolikko <= 100:
        break
    else:
        print("Luvun tulee olla väliltä 1-100")

# Lasketaan paljonko kolikoita tarvitaan
kolikko50 = kolikko // 50
kolikko20 = (kolikko % 50) // 20
kolikko10 = ((kolikko % 50) % 20) // 10
kolikko5 = (((kolikko % 50) % 20) % 10) // 5
kolikko2 = ((((kolikko % 50) % 20) % 10) % 5) // 2
kolikko1 = ((((kolikko % 50) % 20) % 10) % 5) % 2

# printtaa tarvittavien kolikkojen määrän
print("50 snt kolikoita ", kolikko50, " kpl")
print("20 snt kolikoita ", kolikko20, " kpl")
print("10 snt kolikoita ", kolikko10, " kpl")
print("5 snt kolikoita  ", kolikko5, " kpl")
print("2 snt kolikoita  ", kolikko2, " kpl")
print("1 snt kolikoita   ", kolikko1, " kpl")
