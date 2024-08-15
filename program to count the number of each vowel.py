vow = "aeiou"

sent = input("enter a text: ")
count = 0

for s in sent:
  s = s.lower()
  if s in vow:
    count += 1

print(count)