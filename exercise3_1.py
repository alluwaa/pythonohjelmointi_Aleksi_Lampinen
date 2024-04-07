#Kysytään luvut käyttäjältä
print("Anna ensimmäinen luku: ")
luku1 = int(input())
print("Anna toinen luku: ")
luku2 = int(input())

# Verrataan lukuja ja kerrotaan tuloksen perusteella käyttäjälle tieto
if luku1 > luku2:
    print("Suurempi luku = ", luku1)
elif luku2 > luku1:
    print("Suurempi luku = ", luku2)
else:
    print("Numerot ovat yhtä suuria.")