from array import *
n = int(input("sidor:"))
h = int(input("lodrätt:"))
v = int(input("vågrätt:"))
arr = array("i",[4*v*h, 4*v*(n-h), 4*h*(n-v),4*(n-v)*(n-h)])
for i in range(3):
    if arr[0] <= arr[1]:
        arr.remove(arr[0])
    else: arr.remove(arr[1])
print(arr)