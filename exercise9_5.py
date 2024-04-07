import functions

while True:
    print("Valitse toimenpide (1-3), 0 lopettaa ohjelman:")
    toimenpide = int(input())
    if toimenpide == 1:
        print("Anna laatikon leveys:")
        width = int(input())
        print("Anna laatikon korkeus:")
        height = int(input())
        print("Anna laatikon syvyys:")
        depth = int(input())
        print("Laatikon tilavuus: " + str(functions.box_volume(width, height, depth)) + " m3")
    elif toimenpide == 2:
        print("Anna pallon säde:")
        radius = int(input())
        print("Pallon tilavuus :" + str(functions.ball_volume(radius)) + " m3")
    elif toimenpide == 3:
        print("Anna putken säde:")
        radius = int(input())
        print("Anna putken pituus:")
        lenght = int(input())
        print("Putken tilavuus :" + str(functions.pipe_volume(radius, lenght)) + " m3")
    elif toimenpide == 0:
        print("Kiitos ohjelnman käytöstä!")
        break
    else:
        print("Valitse toimenpide (1-3), 0 lopettaa ohjelman:")