p1 = str(input())
p2 = str(input())
p1 = p1.split(" ")
p2 = p2.split(" ")
p1dice = (int(p1[0])+int(p1[1]))/2 + (int(p1[2])+int(p1[3]))/2
p2dice = (int(p2[0])+int(p2[1]))/2 + (int(p2[2])+int(p2[3]))/2
if p1dice == p2dice:
    print("Tie")
elif p1dice > p2dice:
    print("Gunnar")
else:
    print("Emma")