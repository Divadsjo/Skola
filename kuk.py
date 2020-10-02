a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
inmatning = str(input("Skriv: "))
inmatning = inmatning.split(" ") 
print(inmatning)
i = int(inmatning.pop(0))
str = str(inmatning[0])
str = str.upper()
print(str, i)
letList = []
while i > 28:
    i = i - 28
for x in range(len(str)):
    pos = a.find(str[x])
    if str[x] in letList:
        continue
    str = str.replace(str[x], pos+i)
    letList.append((str[::-1])1