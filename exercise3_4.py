    #Kysytään määrä + hinta käyttäjältä
print("Anna rahaa:")
raha_maara = int(input())
print("Ostosten hinta:")
hinta = int(input())

    #Tarkistetaan riittääkö rahat
if raha_maara >= hinta:
    print("Kiitos.")
    print(raha_maara - hinta)
else:
    #Jos ei riitä pyydetään lisää
    lisaa_rahaa = int(input())
    
    #Tehdään uusi tarkistust riittävätkö rahat
    if raha_maara + lisaa_rahaa >= hinta:
        print("Kiitos.")
        print(raha_maara + lisaa_rahaa - hinta)
        #jos ei vieläkään ole rahaa ilmoitetaan käyttäjälle siitä
    else:
        print("Sinulla ei ole tarpeeksi rahaa.")