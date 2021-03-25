import random
dif = str(input("Välj svårighetsgrad skriv en bokstav, E = easy (1-10), M = medium(1-50), H = hard(1-100): "))
if dif == "E":
    r = 10
    extrempunkt = 3
elif dif == "M":
    r = 50
    extrempunkt = 5
elif dif == "H":
    r = 100
    extrempunkt = 7
nummer = int(random.randrange(1, r))
försök = 0
while True:
    inp = int(input("Gissning (skriv 0 för hint): "))
    minmax = int(random.randrange(1, extrempunkt))
    max = nummer + minmax
    min = nummer -(extrempunkt-minmax) + 1
    if inp == 0:
        print("talet är mellan", min,"-",max)
        continue
    elif inp == nummer:
        print("Du gissade rätt!")
        break
    else:
        print("Du gissade fel, försök igen")
        försök += 1  
        if försök == 5:
            break
            print("Du förlorade")
# Först sätt in t och d i en lista
# hitta punkter då 
# sen gör en loop som prövar med en chef
# först pröva om d2 = t så prioritera den