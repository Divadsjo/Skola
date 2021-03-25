fmrom array import *
min = 2
max = 10000
ett = 1
while True:
  try:
    n = int(input("Sidor:"))
  except ValueError:
    print("inte ett tal")
    continue

  if n not in range(min, max + 1):
    print("inte i rätt omfång")
    continue
  break
while True:
  try:
    h = int(input("lodrätt:"))
  except ValueError:
    print("inte ett tal")
    continue

  if h not in range(ett, n + 1):
    print("inte i rätt omfång")
    continue
  break
while True:
  try:
    v = int(input("Vågrätt:"))
  except ValueError:
    print("inte ett tal")
    continue

  if v not in range(ett, n + 1):
    print("inte i rätt omfång")
    continue
  break
arr = array("i",[4*v*h, 4*v*(n-h), 4*h*(n-v),4*(n-v)*(n-h)])
for i in range(3):
    if arr[0] <= arr[1]:
        arr.remove(arr[0])
    else: arr.remove(arr[1])
print(arr)