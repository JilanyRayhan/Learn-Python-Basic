def merge_ar(ar1,ar2):
  ar1.extend(ar2)
  mer = []
  for element in ar1:
    if element not in mer:
      mer.append(element)
  mer.sort()

  return mer

name = [7,39,11,84,3,53]
num = [1,9,5,0,45,54]
print(merge_ar(name,num))