from array import *
n = int(input("sidor:"))
h = int(input("lodrätt:"))
v = int(input("vågrätt:"))
arr = array("i",[4*v*h, 4*v*(n-h), 4*h*(n-v),4*(n-v)*(n-h)])
print(arr)
j = 1
for i in range(3):
    print(i, j)
    if arr[i] <= arr[j]:
        arr.remove(arr[i])
    j = j+1
print(arr)