n = int(input("Antal: "))
for x in range(n):
    if 1*2**x >= n:
        print(x, "dagar")
        break