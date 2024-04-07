def pisteen_arvosana(pisteet):
    if pisteet < 0 or pisteet > 100:
        print("Pistemäärä ei ole mahdollinen")
        return
    elif pisteet >= 91:
        return "Arvosana: 5"
    elif pisteet >= 81:
        return "Arvosana: 4"
    elif pisteet >= 71:
        return "Arvosana: 3"
    elif pisteet >= 61:
        return "Arvosana: 2"
    elif pisteet >= 51:
        return "Arvosana: 1"
    else:
        return "Arvosana: 0"

print("Anna pistemäärä:")
piste_maara = int(input())
arvosana = pisteen_arvosana(piste_maara)
print(arvosana)