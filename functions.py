import math

def show_personal_info():
    nimi = "Matti Meikäläinen"
    kotipaikka = "Sodankylä"
    ammatti = "Ohjelmistosuunnittelija"
    print(nimi)
    print(kotipaikka)
    print(ammatti)

def count_seconds(hours, minutes, seconds):
    total = 0
    total += hours * 60 * 60
    total += minutes * 60
    total += seconds
    return total

def box_volume(width, height, depth):
    tulos = width * height * depth
    return format(tulos, '.2f')
def ball_volume(radius):
    tulos = (4 * math.pi * radius ** 3)/ 3
    return format(tulos, '.2f')
def pipe_volume(radius, lenght):
    tulos = math.pi * radius ** 2 * lenght
    return format(tulos, '.2f')

def show_numbered_list(title, data):
    print(title)
    for i, nimet in enumerate(data, 1):
        print(f"{i}. {nimet}")

def magazine_serial_check(serial):
    if serial[4] == '-': #jos viides merkki on viiva
        serial = serial.replace('-', '') #poistetaan viiva
        if len(serial) == 8 and serial.isdigit(): #tarkistetaanko onko 8 merkkiä pitkä ja pelkästään numeroita
            return True #palautetaan true
    return False #jos ei palautetaan false