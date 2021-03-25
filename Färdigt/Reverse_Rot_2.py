a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
inmatning = str(input("Skriv: "))
inmatning = inmatning.split(" ") 
i = int(inmatning.pop(0))
ord = str(inmatning[0])
ord = ord.upper()
list = []
for x in range(len(ord)):
    list.append(ord[x])
for x in range(len(list)):
    pos = a.find(list[x])
    list[x] = a[pos+i]
list.reverse()
b = ""
for x in range(len(list)):
    b = b + list[x]
print(b)