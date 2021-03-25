import random
##1. randomisera ett tal
randomTal = int(random.random()*10+1)
print(randomTal)
##2. ta in en gissning

##3. Jämför gissningen
for x in range(5):
    Gissning = int(input("Gissning:"))
    if randomTal == Gissning:
        ##3a. om rätt svar: spelaren har vunnit
        print("Du vann! poggers")
        break ## för att sluta loopen
    else:
        print("Du hade fel, dumbom alert")
        ##3b. om fel svar: spelaren har förlorat