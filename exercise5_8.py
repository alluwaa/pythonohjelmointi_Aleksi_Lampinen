#Salaus funktio
def salaus(salasana, siirtoluku):
    salattu_sana = ""
    for kirjain in salasana:
        if kirjain.isalpha(): #Tarkistetaan onko aakkonen
            kirjain1 = ord(kirjain) + siirtoluku #Muutetaan järjestystä siirtoluvun verran
            salattu_sana += chr(kirjain1) #korvataan kirjain
        else:
            salattu_sana += kirjain1
    return salattu_sana

print("Anna salasana:")
salasana = input()
print("Anna siirtoluku:")
siirtoluku = int(input())  
salattu_sana = salaus(salasana, siirtoluku)
print("Salattu sana:", salattu_sana)
