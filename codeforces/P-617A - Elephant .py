distance = int(input())
steps = 0
if distance > 0:
  q = int(distance / 5)
  r = distance % 5
  if r != 0:
    steps = q + 1
  else:
    steps = q
print(steps)