headgear = 0
eyewear = 0
face = 0
tries = int(input("Försök: "))
for x in range(tries):
    antalPlag = int(input("Kläddespel: "))
    for y in range(antalPlag):
        plag = str(input())
        plag = plag.split(" ")
        if plag[1] == "headgear":
            headgear += 1
        elif plag[1] == "eyewear":
            eyewear += 1
        elif plag[1] == "face":
            face += 1
    print(face*eyewear*headgear+face+eyewear+headgear)