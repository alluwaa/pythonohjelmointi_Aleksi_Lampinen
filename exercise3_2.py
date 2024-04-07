#Kysytään käyttäjältä päivän lämpötila
print("Syötä päivän lämpötila")
aste = int(input())

#Tulostetaan vaihtoehto lämpötilan mukaisesti
if aste >= 0 and aste <= 10:
    print("KYLMÄÄ")
elif aste >= 11 and aste <= 15:
    print("KOLEAA")
elif aste >= 16 and aste <= 20:
    print("NORMAALI LÄMPÖTILA")
elif aste >= 21 and aste <= 25:
    print("LÄMMINTÄ")
elif aste >= 26 and aste <= 30:
    print("HELLETTÄ")
else:
    print("Lämpötila ei ole kesäpäivän asteikko alueella")