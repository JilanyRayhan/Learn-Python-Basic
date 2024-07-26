rating = {10 : 300, 11 : 213, 12 : 456, 14 : 544, 15 : 653}
add = {16 : 768}
rating.update(add)
rating.update({17: 888})
rating.pop(11)
rating[18] = 999
emp = {}
print(rating)
print(rating.items())
print(rating[10])
print(rating.get(19))
print(emp)
print(rating.values())
print(rating.keys())
del rating[16]

for key in rating.keys():
  print(key)

for key in rating.keys():
  print(rating[key])

for value in rating.values():
  print(value)

for key,value in rating.items():
  print(key,value)