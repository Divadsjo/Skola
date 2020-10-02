min = 1
max = 100

while True:
  try:
    value = int(input("Tal:"))
  except ValueError:
    print("inte ett tal")
    continue

  if value not in range(min, max + 1):
    print("inte i rätt omfång")
    continue
  break
for x in range(1, value+1):
    print(x, "Abracadabra")
