import functions

print ("Syötä tapahtuman osallistujat pilkulla eroteltuna: ")
data = input().split(',') 
data = [p.strip() for p in data]
functions.show_numbered_list("Ilmoittautumisjärjestys:", data)
data = sorted(data)
functions.show_numbered_list("Aakkosjärjestys etunimen perusteella:", data)
data = sorted([" ".join(reversed(p.split(" "))) for p in data])
functions.show_numbered_list("Aakkosjärjestys sukunimen perusteella:", data)