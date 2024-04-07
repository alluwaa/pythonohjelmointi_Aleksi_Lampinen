import functions

print("Anna ISSN-sarjanumero:")
serial = input()
if functions.magazine_serial_check(serial):
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")