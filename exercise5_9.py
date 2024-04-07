nimet = ["Aleksi", "Antti", "Pekka", "Matti", "Jarmo", "Esa", "Timo", "Topi", "Pertti", "Benjamin"]

tulos = nimet

tulos = [nimi for nimi in tulos if 's' not in nimi] #Poistetaan s kirjaimet

tulos = [nimi for nimi in tulos if 'e' not in nimi] #Poistetaan e kirjaimet

tulos = [nimi for nimi in tulos if len(nimi) < 8] #Poistetaan alle 8 merkkiä

tulos = [nimi for nimi in tulos if sum(1 for kirjain in nimi if kirjain in 'aeiou') <= 2] #Poistetaan tupla vokaalit

# Tulosta tulos
print(tulos)
