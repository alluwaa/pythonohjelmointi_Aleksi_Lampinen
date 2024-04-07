print("Anna hinta ilman alv: ")
alviton = float(input())

alv = 24 / 100
alvillinen = alviton * (1 + alv)

print("Hinta alv:n kanssa: {:.2f}".format(alvillinen) + " €")