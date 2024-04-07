import math

while True:
    print ("Anna säde: ")
    sade = float(input())
    pinta_ala = math.pi * sade**2
    print("Ympyrän pinta-ala on: ", round(pinta_ala, 2))
    print ("Haluatko jatkaa? (k/e)")
    jatko = input()
    if jatko == "e":
        break




