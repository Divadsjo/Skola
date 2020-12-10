#0. Ge instruktioner på hur programet funkar
#1. ta ett ord på random sätt
#2. Gör en varibal mer original ordet och en som är tom med det man gissar.
#3. Ta in en gissning och se om den finns i original ordet
#   3a. Om den finns byt ut alla instanser av den i det tomma ordet med hjälp av
#   index som ligger i en list
#   3b. om den inte finns så lägg till en lem på gubben och räkna ner gissningarna.
#4a. om man kom på ordet så skriv nåt grattis meddelande
#4b. Om man inte kom på ordet skriv nåt meddelande och kanske repetera hela programet.  
ord = list(input("Välj ett ord:").lower())
gissningarKvar = 11
gissning = []
bokstavIndex = []
felSvar = []
for x in range(len(ord)):
    if ord[x] == " ":
        gissning.append(" ")
        continue
    else:
        gissning.append("_")
print(ord, gissning)
while True:
    bokstav = str(input("Gissning: ")).lower()
    if ord.count(bokstav) == 0:
        gissningarKvar -= 1
        felSvar.append(bokstav)
        print("".join(gissning))
        print("Fel!", "Antal fel svar tills förlust", gissningarKvar, "Felaktigta bokstäver:", felSvar)
    else:
        for y in range(len(ord)):
            if ord[y] == bokstav:
                gissning[y] = bokstav
            else:
                continue
        print("".join(gissning))
        print("Rätt!", "Antal fel svar tills förlust:", gissningarKvar, "Felaktigta bokstäver:", felSvar)
    if gissningarKvar == 0:
        break
    elif gissning == ord:
        print("Wohoo du gissade på rätt ord!")
        break
        