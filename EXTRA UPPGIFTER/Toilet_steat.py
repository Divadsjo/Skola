status = ""
inp = str(input())
a = 0
for x in range(1, 3):
    status = inp[0]
    r = x
    for x in range(1, len(inp)):
        if inp[x] == status:
            print("rätt")
            if r == 1 and status == "D":
                status = "D"
                a += 1
            elif r == 2 and status == "U":
                status = "U"
                a += 1
        else:
            print("fel")
            a += 1
            status = inp[x]
            if r == 1 and status == "D":
                status = "D"
                a += 1
            elif r == 2 and status == "U":
                status = "U"
                a += 1
    print(a)
    a = 0