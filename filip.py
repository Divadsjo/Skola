from array import *
x = str(input("Tal 1:"))
y = str(input("Tal 2:"))
x = x[2] + x[1] + x[0]
y = y[2] + y[1] + y[0]
x = int(x)
y = int(y)
if x < y: 
    print(y)
elif x > y:
    print(x)
else: 
    print("de är lika stora")



# if len(x) > len(y):
#     x = x[2] + x[1] + x[0]
#     print(x)
# elif len(y) > len(x):
#     y = y[2] + y[1] + y[0]
#     print(y)
# else:
