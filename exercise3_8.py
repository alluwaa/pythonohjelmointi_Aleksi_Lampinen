# Funktio loppusumman laskemiselle
def laske_loppusumma(summa, onko_opiskelija, onko_kanta_asiakas, pisteet, alennuskoodi):
    #Jos alennuskoodi annetaan 10% alennus
    if alennuskoodi == "FALL23":
        summa *= 0.9
    #Toinen alennuskoodi jossa 20%
    elif alennuskoodi == "BK2SCHOOL" and onko_opiskelija == "K":
        summa *= 0.8

    #Jos kanta-asiakas lasketaan piste alennus
    if onko_kanta_asiakas == "K":
        lisa_pisteet = summa // 10 * 100 
        pisteet += lisa_pisteet
        alennus = (pisteet // 1000) * 5
        summa -= alennus
    if summa < 100:
        summa += 7.95
    return summa

#Ohjelma, kysytään käyttäjältä tiedot, lopuksi ajetaan tiedot laske_loppusumma funktioon ja palautetaan käyttäjälle vastaus
print("Anna ostosten kokonaissumma euroina: ")
summa = float(input())
print("Oletko opiskelija? (K/E): ")
onko_opiskelija = input()
print("Oletko kanta-asiakas? (K/E): ")
onko_kanta_asiakas = input()
if onko_kanta_asiakas == "K":
    print("Anna kanta-asiakaspisteet")
    pisteet = float(input())
else:
    pisteet = 0

print("Anna mahdollinen alennuskoodi: ")
alennuskoodi = input()
loppusumma = laske_loppusumma(summa, onko_opiskelija, onko_kanta_asiakas, pisteet, alennuskoodi)

print(str(loppusumma) + " €")