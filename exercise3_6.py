#Tarkistetaan ifelsellä onko karkausvuosi ja palautetaan true tai false 
def tarkista_karkausvuosi(vuosi):
    if vuosi % 400 == 0:
        return True
    elif vuosi % 100 == 0:
        return False
    elif vuosi % 4 == 0:
        return True
    else:
        return False
#Kysytään käyttäjältä vuosiluku ajetaan tarkistus ja ilmoitetaan vastaus käyttäjälle
print("Anna vuosiluku: ")
vuosi = int(input())
if tarkista_karkausvuosi(vuosi):
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")