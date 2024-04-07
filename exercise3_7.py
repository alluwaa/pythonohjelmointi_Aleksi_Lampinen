#Funktio kirjeen hinnan laskemiselle 
def kirje_hinta(paino, mahtuuko_postilaatikkoon):
    perushinta = 0.5
    if paino <= 200:
        lisamaksu = 0
    elif paino <= 500:
        lisamaksu = paino * 4/100
    else:
        lisamaksu = paino * 7/100
    if paino > 500 and mahtuuko_postilaatikkoon == "ei":
        lisamaksu += 200
    return perushinta + lisamaksu / 100

#Funktio paketin hinnan laskemiselle
def paketti_hinta(paino):
    perushinta = 2
    if paino <= 200:
        lisamaksu = 0
    elif paino <= 500:
        lisamaksu = paino * 8/100
    else:
        lisamaksu = paino * 14/100

    return perushinta + lisamaksu / 100

#Ohjelma, kysytään käyttäjältä tiedot ja laitetaan tietojen kanssa funktioon perustuen onko kyseessä kirje vai paketti
print("Anna lähetyksen tyyppi (kirje/paketti): ")
tyyppi = input()

print("Anna paino (gr): ")
paino = float(input())

if tyyppi == "kirje":
    print("Mahtuuko postilaatikkoon? (kyllä/ei): ")
    mahtuuko_postilaatikkoon = input()
    hinta = kirje_hinta(paino, mahtuuko_postilaatikkoon)
    print(f"Lähetyksen hinta: {hinta:.2f} €")

elif tyyppi == "paketti":
    hinta = paketti_hinta(paino)
    print(f"Lähetyksen hinta: {hinta:.2f} €")
else:
    print("Lähetyksen tyyppi tulee olla kirje tai paketti.")


