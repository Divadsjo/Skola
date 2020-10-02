min = 5
max = 15

while True:
  try:
    value = int(input())
  except ValueError:
    print("inte ett tal")
    continue

  if value not in range(min, max + 1):
    print("inte i rätt omfång")
    continue
  break