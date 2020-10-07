olda = "abcdefghijklmnopqrstuvwxyz"
newa = ["@","8","(","|)","3","#","6","[-]","|","_|","|<","1","[]\/[]","[]\[]","0","|D","(,)","|Z","$","']['","|_|","\/","\/\/","}{","´/","2"]
ord = str(input("Skriv: "))
ord = ord.lower()
neword = ""
for x in range(len(ord)):
    if ord[x] in olda:
        neword = neword + newa[olda.find(ord[x])]
    else:
        neword = neword + ord[x]
print(neword)