sen = input("enter a text: ").strip().split(" ")

order = []
for l in range(len(sen)):
  #sen[l] = sen[l].lower()
  order.append(sen[l].lower())
  order.sort()

for o in order:
  print(o)